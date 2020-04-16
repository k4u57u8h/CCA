# Model Training Part
import pandas as pd
import pickle
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

# Loading the dataset
dataset = pd.read_csv('application_record.csv')
dataset = dataset.dropna()
X = dataset.iloc[:, [2,3,5,6,7]].values

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
X[:, 1] = labelencoder_X.fit_transform(X[:, 1])
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
X[:, 4] = labelencoder_X.fit_transform(X[:, 4])

# Applying kmeans to dataset

kmeans = KMeans(n_clusters=2, init='k-means++', n_init=10, max_iter=300, random_state=0)
y_kmeans = kmeans.fit_predict(X)

with open('my_algo.pkl', 'wb') as f:
    pickle.dump(kmeans, f)
