import numpy as np


a = np.array([1, 2, 3])
b = np.array([2, 3, 4])
print(np.concatenate([a,b]))
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

c = data.view()
c[0] = 10
print(data)

# converting map object to set
