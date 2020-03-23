from model import classes_to_pandas
from model import TRAINING_WINDOW_RECORDS
from model import Confidence

import numpy as np
from sklearn import linear_model


class FeeModel():

    def _train(self):
        self._data = classes_to_pandas(self._raw_data[-TRAINING_WINDOW_RECORDS:])
        x = np.array(list(zip(
            self._data[["price"]].values(),
            len(self._data.index) * self._pricing_model.confidence_interval(Confidence.BAND_P99),
            len(self._data.index) * self._pricing_model.confidence_interval(Confidence.BAND_P01),
            len(self._data.index) * self._pricing_model.confidence_interval(Confidence.BAND_P05),
        )))
        y = self._data["fee"].values
        self._model = linear_model.LinearRegression()
        self._model.fit(x, y)

    def __init__(self, pricing_model, data):
        self._raw_data = data
        self._pricing_model = pricing_model
        self._train()

    def update(self, pricing_model, training_data):
        self._raw_data += training_data
        self._pricing_model = pricing_model
        self._train()

    def estimate(self, price):
        return self._model.predict([
            price,
            self._pricing_model.confidence_interval(Confidence.BAND_P99),
            self._pricing_model.confidence_interval(Confidence.BAND_P01),
            self._pricing_model.confidence_interval(Confidence.BAND_P05),
        ])
