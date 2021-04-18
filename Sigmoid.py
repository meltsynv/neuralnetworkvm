import numpy as np


class Sigmoid:

    @staticmethod
    def sigmoid(x):
        val = 1 / (1 + np.exp(-x))  # 1 / 1 + e^-x
        return val

    @staticmethod
    def sigmoid_derivative(x):
        val = Sigmoid.sigmoid(x) * (1 - Sigmoid.sigmoid(x))  # (1 / 1 + e^-x) *  (1 - (1 / 1 + e^-x))
        return val

    @staticmethod
    def matrix(m1):
        mr = np.zeros(shape=(len(m1), len(m1[0])))
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                mr[i][j] = Sigmoid.sigmoid(m1[i][j])
        return mr
