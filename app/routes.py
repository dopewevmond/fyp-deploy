from app import app
from comp_desc.cd import generate_molecular_descriptors as get_desc
import subprocess
import pandas as pd
from flask import render_template, request, flash
from app.forms import ModelForm
from .try_load_pickle import get_pickled_objects

pickled_objects = get_pickled_objects()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    full_names_dict = {"inh": "Inhibitory", "act": "Activatory",
                       "rf": "Random Forest", "adb": "Adaboost"}
    form = ModelForm()
    if form.validate_on_submit():
        scaler = pickled_objects[f"{form.model.data}_{form.class_to_pred.data}_scaler"]
        mask = pickled_objects[f"{form.model.data}_{form.class_to_pred.data}_mask"]
        model = pickled_objects[f"{form.model.data}_{form.class_to_pred.data}_model"]
        X_columns = pickled_objects["X_columns"]

        desc_filename = get_desc(smiles=form.smiles.data)

        error = False
        try:
            df = pd.read_csv(desc_filename, sep="\t", header=0)
            subprocess.run(f"rm ./{desc_filename}", shell=True)
            df.drop(columns=["Number"], axis=1, inplace=True)
            features = scaler.transform(df)
            features = pd.DataFrame(features, columns=X_columns)
            features = features.loc[:, mask]
            inactive_prob, active_prob = model.predict_proba(
                features.to_numpy().reshape(1, -1))[0]
            activity, confidence = True, active_prob
            if inactive_prob > active_prob:
                activity, confidence = False, inactive_prob
            results = {}
            results["smiles"] = form.smiles.data
            results["model"] = full_names_dict[form.model.data]
            results["type_of_activity"] = full_names_dict[form.class_to_pred.data]
            results["activity"] = activity
            results["confidence"] = confidence

            flash("Please scroll to the bottom of the page to see the results", "success")
            return render_template('pred.html', form=form, results=results)

        except pd.errors.EmptyDataError:
            error = "Please make sure the SMILES are valid and try again"
            flash(error, "danger")
            subprocess.run(f"rm ./{desc_filename}", shell=True)

        return render_template('pred.html', form=form)
    return render_template('pred.html', form=form)


@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')


@app.route('/faqs')
def faqs():
    return render_template('faq.html')
