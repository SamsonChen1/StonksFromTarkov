from model import classes_to_pandas
from model import TESTING_FRACTION, SEED, TRAINING_WINDOW_RECORDS, PRIMARY
from model import Confidence

import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

class PricingModel:

    def _train(self):
        self._data = classes_to_pandas(self._raw_data[-TRAINING_WINDOW_RECORDS:])
        x = np.array(list(zip(
            self._data[["ts"]].values(),
        )))
        y = self._data["price"].values
        self._model = dict()
        self._model[PRIMARY] = GradientBoostingRegressor(loss="ls")
        self._model[PRIMARY].fit(x, y)
        for band in [Confidence.BAND_P01, Confidence.BAND_P05, Confidence.BAND_P99]:
            self._model[band] = GradientBoostingRegressor(loss="quantile", alpha=band)
            self._model[band].fit(x, y)

    def __init__(self, data):
        self._raw_data = data
        self._train()

    def update(self, training_data):
        self._raw_data += training_data
        self._train()

    def predict(self):
        return self._model[PRIMARY].predict(self._data[["ts"]].tail(1).values())

    def confidence_interval(self, interval):
        if interval not in self._model:
            raise Exception(f"Cannot predict unknown interval {interval}")
        else:
            return self._model[interval].predict(self._data[["ts"]].tail(1).values())
