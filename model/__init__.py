import pandas as pd

def classes_to_pandas(list_of_classes):
    return pd.DataFrame([vars(s) for s in list_of_classes])

TESTING_FRACTION = 0.2
SEED = 42
TRAINING_WINDOW_RECORDS = 100

PRIMARY = "primary"
class Confidence():
    BAND_P01 = 0.01
    BAND_P05 = 0.05
    BAND_P99 = 0.99
