from sklearn.cluster import KMeans 
import numpy as np 

# Data points
X = np.array([[1.713, 1.586], [0.180, 1.786], [0.353, 1.240], 
              [0.940, 1.566], [1.486, 0.759], [1.266, 1.106],
              [1.540, 0.419], [0.459, 1.799], [0.773, 0.186]])

# Corresponding labels
y = np.array([0, 1, 1, 0, 1, 0, 1, 1, 1])

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

print("The input data is ")
print("VAR1 \t VAR2 \t CLASS")
for i, val in enumerate(X):
    print(val[0], "\t", val[1], "\t", y[i])

# To get test data from the user 
print("The Test data to predict ")
test_data = [] 
VAR1 = float(input("Enter Value for VAR1: ")) 
VAR2 = float(input("Enter Value for VAR2: ")) 
test_data.append(VAR1)
test_data.append(VAR2)

print("The predicted Cluster is:", kmeans.predict([test_data]))
