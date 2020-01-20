import csv

import pandas as pd
import numpy as np
from numpy import random


def handle_uploaded_file_for_lr(file_object, x_col_index, y_col_index, theta_col_index):
    y_col_index = y_col_index + 1
    theta_col_index = y_col_index + theta_col_index + 1
    x_col_index = theta_col_index + x_col_index + 1
    csv_file = pd.read_csv(file_object, header=0, index_col=False, usecols=[y_col_index, theta_col_index, x_col_index])
    for row in csv_file:
        print(row)


def gradient_descent(x, y, theta, alpha, m, num_of_iteration):
    x_trans = x.transpose()

    for i in range(0, num_of_iteration):
        hypothesis = np.dot(x, theta)
        loss = hypothesis - y
        cost = np.sum(loss ** 2) / (2 * m)
        #print("Iteration %d | Cost: %f" % (i, cost))
        gradient = np.dot(x_trans, loss) / m
        theta = theta - alpha * gradient

    return theta


def genData(numPoints, bias, variance):
    x = np.zeros(shape=(numPoints, 2))
    y = np.zeros(shape=numPoints)

    # basically a straight line
    for i in range(0, numPoints):
        # bias feature
        x[i][0] = 1
        x[i][1] = i
        # our target variable
        y[i] = (i + bias) + random.uniform(0, 1) * variance

    return x, y

path = '/Users/guangshuai/myDjango/myDemo/media/EXAMPLE_DATA_FOR_LELIA.csv'

handle_uploaded_file_for_lr(path, 5, 0, 0)

# x, y = genData(100, 25, 10)
# print("x: " + np.array_str(x) + "\ny: " + np.array_str(y))
# m, n = np.shape(x)
# numIterations = 100000
# alpha = 0.0005
# theta = np.ones(n)
# theta = gradient_descent(x, y, theta, alpha, m, numIterations)
# print(theta)
