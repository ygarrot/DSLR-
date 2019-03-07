import pandas as pd
import numpy as np
import csv
from Ft_logistic_regression import Ft_logistic_regression


def get_value(thetas, elem):
    test = [1] + elem[2:]
    for i, v in enumerate(test):
        if np.isnan(v):
            test[i] = 0
    return np.dot(thetas, test)

def predict():
    raw_data = pd.read_csv('data/dataset_test.csv',delimiter=',')
    data = raw_data.drop(columns = ['First Name', 'Last Name', 'Birthday', 'Best Hand'])
    data = data.drop(columns = ['Arithmancy', 'Care of Magical Creatures', 'Astronomy'])
    hogwarts = data.copy()
    for key in hogwarts:
        if key != 'Index' and key != 'Hogwarts House':
            hogwarts = hogwarts.drop(columns = [key])
    houses = [None] * 4
    thetas = np.genfromtxt('thetas.csv', delimiter=',')
    for elem in hogwarts['Index']:
        test = data.loc[elem].tolist()
        i = 2
        for key in data:
            if key != 'Index' and key != 'Hogwarts House':
                test[i] = (test[i] - min(data[key])) / (max(data[key]) - min(data[key]))
                i += 1
        houses[0] = get_value(thetas[0], test)
        houses[1] = get_value(thetas[1], test)
        houses[2] = get_value(thetas[2], test)
        houses[3] = get_value(thetas[3], test)
        if (houses[0] > houses[1] and houses[0] > houses[2] and houses[0] > houses[3]):
            hogwarts.loc[elem, 'Hogwarts House'] = 'Gryffindor'
        elif (houses[1] > houses[2] and houses[1] > houses[3]):
            hogwarts.loc[elem, 'Hogwarts House'] = 'Slytherin'
        elif (houses[2] > houses[3]):
            hogwarts.loc[elem, 'Hogwarts House'] = 'Hufflepuff'
        else:
            hogwarts.loc[elem, 'Hogwarts House'] = 'Ravenclaw'
    file_content  = hogwarts.to_csv(index=False)
    f = open('houses.csv', 'w+')
    f.write(file_content)
    f.close()
def main():
    predict()

if __name__ == '__main__':
    main()
