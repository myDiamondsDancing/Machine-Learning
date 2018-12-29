from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print("Ключи cancer(): \n{}".format(cancer.keys()))

#####################################################################################################

print("Форма массива data для набора cancer: {}".format(cancer.data.shape))

#####################################################################################################

print("Признаки: {}".format(cancer.feature_names))

#####################################################################################################

print(cancer.DESCR)

#####################################################################################################

print(cancer.data[:2])

#####################################################################################################

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer() 

X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
print(X_train.shape)

#####################################################################################################

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)

#####################################################################################################
clf.fit(X_train, y_train)

#####################################################################################################

print("Прогнозы на тестовом наборе: {}".format(clf.predict(X_test[:5])))

#####################################################################################################

print("Правильность на тестовом наборе: {:.2f}".format(clf.score(X_test, y_test)))

#####################################################################################################

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
 cancer.data, cancer.target, stratify=cancer.target, random_state=66)
training_accuracy = []
test_accuracy = []
# пробуем n_neighbors от 1 до 10
neighbors_settings = range(1, 11)

for n_neighbors in neighbors_settings:
     #Строим модель
     clf = KNeighborsClassifier(n_neighbors=n_neighbors)
     clf.fit(X_train, y_train)
     #Записываем правильность на обучающем наборе
     training_accuracy.append(clf.score(X_train, y_train))
     #Записываем правильность на тестовом наборе
     test_accuracy.append(clf.score(X_test, y_test))
plt.plot(neighbors_settings, training_accuracy, label="правильность на обучающем наборе")
plt.plot(neighbors_settings, test_accuracy, label="правильность на тестовом наборе")
plt.ylabel("Правильность")
plt.xlabel("количество соседей")
plt.legend()
print('Done')
