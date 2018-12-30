import pandas as pd
import numpy as np
file = pd.read_csv('E:\datasets\sf-salaries\Salaries.csv', sep=',')

file

##########################################################################################

file = file[:120000]
file

##########################################################################################

file.columns.values.tolist()

##########################################################################################

file.Benefits.fillna(0, inplace=True)
file

##########################################################################################

target = file.JobTitle

file = file.drop('JobTitle', axis=1)

feature_names = file.columns.values.tolist()
feature_names

##########################################################################################

data = np.array(file)
data

##########################################################################################

def code(target):
    i = 0
    codes = {}
    data = list()
    
    for key in target:
        if not key in codes:
            codes[key] = i
            i += 1
            
    for value in target:
        data.append(codes[value])
        
    return np.array(data)

target = code(target)
target

##########################################################################################

target_names = 'JobTitle'
target_names

##########################################################################################

from collections import namedtuple

DataSet = namedtuple('DataSet', 'target_names target DESCR data feature_names')

my_dataset = DataSet(target_names, target, '', data, feature_names)
my_dataset

##########################################################################################

import pickle
with open('C:\Python for beginners\ML\data.pickle', 'wb') as f:
    pickle.dump(my_dataset, f)
