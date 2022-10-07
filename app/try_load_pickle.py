import pickle

# loading the pickles for adaboost

with open("ml_pickled/adb_act_scaler", "rb") as file:
    adb_act_scaler = pickle.load(file)
with open("ml_pickled/adb_act_mask", "rb") as file:
    adb_act_mask = pickle.load(file)
with open("ml_pickled/adb_act_model", "rb") as file:
    adb_act_model = pickle.load(file)

with open("ml_pickled/adb_inh_scaler", "rb") as file:
    adb_inh_scaler = pickle.load(file)
with open("ml_pickled/adb_inh_mask", "rb") as file:
    adb_inh_mask = pickle.load(file)
with open("ml_pickled/adb_inh_model", "rb") as file:
    adb_inh_model = pickle.load(file)

with open("ml_pickled/rf_act_scaler", "rb") as file:
    rf_act_scaler = pickle.load(file)
with open("ml_pickled/rf_act_mask", "rb") as file:
    rf_act_mask = pickle.load(file)
with open("ml_pickled/rf_act_model", "rb") as file:
    rf_act_model = pickle.load(file)

with open("ml_pickled/rf_inh_scaler", "rb") as file:
    rf_inh_scaler = pickle.load(file)
with open("ml_pickled/rf_inh_mask", "rb") as file:
    rf_inh_mask = pickle.load(file)
with open("ml_pickled/rf_inh_model", "rb") as file:
    rf_inh_model = pickle.load(file)

with open("ml_pickled/X_columns", "rb") as file:
    X_columns = pickle.load(file)


def get_pickled_objects():
    return {
        "adb_act_scaler": adb_act_scaler,
        "adb_act_mask": adb_act_mask,
        "adb_act_model": adb_act_model,
        "adb_inh_scaler": adb_inh_scaler,
        "adb_inh_mask": adb_inh_mask,
        "adb_inh_model": adb_inh_model,
        "rf_act_scaler": rf_act_scaler,
        "rf_act_mask": rf_act_mask,
        "rf_act_model": rf_act_model,
        "rf_inh_scaler": rf_inh_scaler,
        "rf_inh_mask": rf_inh_mask,
        "rf_inh_model": rf_inh_model,
        "X_columns": X_columns
    }
