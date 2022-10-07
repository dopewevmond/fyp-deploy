from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class ModelForm(FlaskForm):
    smiles = StringField('SMILES', validators=[DataRequired(
        message="Please enter a valid SMILES string")])
    model = SelectField('Algorithm', choices=[(
        'rf', 'Random Forest'), ('adb', 'Adaboost')], validators=[DataRequired()])
    class_to_pred = SelectField('Action on human alpha-Glucosidase', choices=[(
        'act', 'Activatory'), ('inh', 'Inhibitory')], validators=[DataRequired()])
    submit = SubmitField('Predict')
