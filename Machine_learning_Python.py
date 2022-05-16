#Import Libraries
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

#Upload the dataset
dataset = pd.read_csv('.../TaxaCombined.csv', sep='\t')

#Describtion of the data
dataset.describe()

#Target column names
dataset['disease_state'].unique()

#Select the features (bacterial names columns) and the target labels (disease state column)
labels = dataset['disease_state']
features = dataset.drop('disease_state',axis=1)

#Normalization:
# Creating an Object of StandardScaler
scaler = MinMaxScaler()

# Fit the dataframe to the scaler
print(scaler.fit(features))

# Transform the dataframe
features_scaled = scaler.transform(features)

# Convert the scaled array to dataframe
features_scaled = pd.DataFrame(features_scaled, columns=features.columns)

# Correlation by Heatmap
f,ax = plt.subplots(figsize=(20,25))
sns.heatmap(features_scaled.corr(), annot=True, linewidths=.5, fmt= '.1f',ax=ax)

#Grid search using n_neighbors = 1:40 
accuracy_rate = []
# Range of n_neighbors for KNN
for i in range(1,40):
    knn = KNeighborsClassifier(n_neighbors=i, metric='minkowski',weights='uniform')
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
    accuracy_rate.append(scores.mean())

#Plotting accuracy scores for 40 neighbors
plt.figure(figsize=(12,6))
accuracy_plot = plt.plot(range(1,40), accuracy_rate, color='blue', linestyle='dashed', marker='o',
    markerfacecolor='red', markersize=10)
accuracy_plot = plt.title('Accuracy Rate vs. K Value')
accuracy_plot = plt.xlabel('N_neighbors')
accuracy_plot = plt.ylabel('Accuracy Rate')

#Go with 16 neighbours
knn = KNeighborsClassifier(n_neighbors=16)

## Fit the model
knn.fit(X_train, y_train)

## Predict the values
pred = knn.predict(X_test)

# Classification Report and Confusion Matrix
print("Classification Report\n",classification_report(y_test, pred),
"\n\nConfusion Matrix\n",confusion_matrix(y_test, pred))

# Accuracy Score for whole of Test Data
print("Accuracy Score",accuracy_score(y_test, pred))
