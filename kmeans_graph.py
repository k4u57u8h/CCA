# Visualization Part
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

dataset_visual = pd.read_csv('application_record.csv')
dataset_visual = dataset_visual.dropna()
X_visual = dataset_visual.iloc[:, [3,5]].values

labelencoder_X_visual = LabelEncoder()
X_visual[:, 0] = labelencoder_X_visual.fit_transform(X_visual[:, 0])

sc_X = StandardScaler()
X_visual = sc_X.fit_transform(X_visual)

kmeans_visual = KMeans(n_clusters=2, init='k-means++', n_init=10, max_iter=300, random_state=0)
y_kmeans_visual = kmeans_visual.fit_predict(X_visual)

# Visulaizing the clusters
plt.scatter(X_visual[y_kmeans_visual == 0, 0], X_visual[y_kmeans_visual == 0, 1], s=100, c='red', label='No')
plt.scatter(X_visual[y_kmeans_visual == 1, 0], X_visual[y_kmeans_visual == 1, 1], s=100, c='blue', label='Yes')
plt.title('Clusters of Approval')
plt.xlabel('Owns a house or not')
plt.ylabel('Income')
plt.legend()
plt.show()