import json
import pickle as pkl

import numpy as np
import pandas as pd

# pip install sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# type(dataset) = Bunch
dataset = load_iris()

# type(df) = pd.DataFrame
df = pd.DataFrame(dataset.data)

# Установка заголовков и меток классов
df.columns = dataset.feature_names
df['Target'] = dataset.target

# type(data) = np.ndarray
data = df.values

numpy_output_file_name = 'numpy.out'

shape = data.shape

# NumPy --------------------------------------------------

# Загрузка массива в файл
# Вы также можете указать название файла вместо f
with open(numpy_output_file_name, 'w') as f:
    data.tofile(f, sep=',')

# Загрузка массива из файла в программу
with open(numpy_output_file_name, 'r') as f:
    data = np.fromfile(f, sep=',')
    data.shape = shape

# Pandas--------------------------------------------------

pandas_output_file_name = 'pandas.csv'
df.to_csv(pandas_output_file_name, sep=',', header=df.columns)

df = pd.read_csv(pandas_output_file_name, sep=',')

# Обучение модели ----------------------------------------

X_train, X_test, y_train, y_test = train_test_split(dataset.data,
                                                    dataset.target,
                                                    test_size=0.1)

lasso = LogisticRegression(C=1)

lasso.fit(X_train, y_train)

# type(params) = dict
params = lasso.get_params()

score = lasso.score(X_test, y_test)

# JSON -----------------------------------------------------

json_output_file_name = 'json.json'

# Загрузка словаря в файл
with open(json_output_file_name, 'w') as f:
    json.dump(params, f, separators=(',', ':'))

with open(json_output_file_name, 'r') as f:
    params = json.load(f)

# Проверка модели

lasso = LogisticRegression(C=1)
lasso.set_params(**params)
lasso.fit(X_train, y_train)

assert(score == lasso.score(X_test, y_test))

# Pickle --------------------------------------------
pickle_output_file_name = 'pickle.pickle'

with open(pickle_output_file_name, 'wb') as f:
    pkl.dump(params, f)

with open(pickle_output_file_name, 'rb') as f:
    params = pkl.load(f)

# Проверка модели

lasso = LogisticRegression(C=1)
lasso.set_params(**params)
lasso.fit(X_train, y_train)

assert(score == lasso.score(X_test, y_test))

print('Мы успешно завершили "консервацию"!')
