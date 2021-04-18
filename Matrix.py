import numpy as np
import random


class Matrix:
    @staticmethod
    def sub(m1, m2):
        mr = np.zeros(shape=(len(m1), len(m1[0])))
        if isinstance(m2, list):
            for i in range(len(m1)):
                for j in range(len(m1[i])):
                    mr[i][j] = m1[i][j] - m2[i][j]
            return mr
        else:
            for i in range(len(m1)):
                for j in range(len(m1[i])):
                    mr[i][j] = m1[i][j] - m2[i][j]
            return mr

    @staticmethod
    def add(m1, m2):
        mr = np.zeros(shape=(len(m1), len(m1[0])))
        if isinstance(m2, list):
            for i in range(len(m1)):
                for j in range(len(m1[i])):
                    mr[i][j] = m1[i][j] + m2[i][j]
            return mr
        else:
            for i in range(len(m1)):
                for j in range(len(m1[i])):
                    mr[i][j] = m1[i][j] + m2[i][j]
            return mr

    @staticmethod
    def mult(m1, m2):
        if isinstance(m2, list):
            if (len(m1) != len(m2)) | (len(m1[0]) != len(m2[0])):
                mr = np.zeros(shape=(len(m1), len(m2[0])))
                for i in range(len(mr)):
                    for j in range(len(mr[i])):
                        sum = 0
                        for k in range(len(m1[0])):
                            sum = sum + (m1[i][k] * m2[k][j])
                        mr[i][j] = sum
                return mr
            else:
                mr = np.zeros(shape=(len(m1), len(m1[0])))
                for i in range(len(m1)):
                    for j in range(len(m1[i])):
                        mr[i][j] = m1[i][j] * m2[i][j]
                return mr
        else:
            mr = np.zeros(shape=(len(m1), len(m1[0])))
            for i in range(len(m1)):
                for j in range(len(m1[i])):
                    mr[i][j] = m1[i][j] * m2
            return mr

    @staticmethod
    def randomize(row, col):
        mr = np.zeros(shape=(row, col))
        for i in range(len(mr)):
            for j in range(len(mr[i])):
                mr[i][j] = random.uniform(-1, 1)
        return mr

    @staticmethod
    def transpose(m1):
        mr = np.zeros(shape=(len(m1[0]), len(m1)))
        for i in range(len(m1)):
            for j in range(len(m1[i])):
                mr[j][i] = m1[i][j]
        return mr
