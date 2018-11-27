import numpy as np
#from matplotlib.pyplot import * 
from pylab import *

def pprint(arr):
    print("type:{}".format(type(arr)))
    print("shape: {}, dimension: {}, dtype:{}".format(arr.shape, arr.ndim, arr.dtype))
    print("Array's Data:\n", arr)


'''
arr = [(1, 2, 3), (4, 5, 6)]
a = np.array(arr, dtype=float)
b= np.zeros((4,5))
c= np.ones((4,5), dtype=np.int16)
d= np.full((4,5),7)
e= np.eye(5)
#pprint(a)
print(e)


a = np.linspace(0,1,5)
b = np.arange(0, 10, 2, float)
c = np.logspace(0.1, 1, 20, float)
pprint(c)
plot(c, 'o')
show()

data = np.random.normal(0, 0.1, 10000)
data2 = np.random.rand(10000)
data3 = np.random.randn(10000)
data4 = np.random.randint(-100, 100, 10000)
data5 = np.random.random(10000)
hist(data4, bins=10)
show()



a = np.random.randint(0,10,(2,3))
b = np.random.randint(0,10,(2,3))

np.save("result/my array1", a)
np.save("result/my array2", a,b)
print(a)

a = np.random.randint(0,10,(2,3))
b = np.random.randint(0,10,(2,3))
np.savez("../result/my array2", a,b)

print(a,b)

a = np.load("../result/my array2.npz")

print(a['arr_0'])

a = np.loadtxt("../data/data.txt", np.int)
print(a)


data = np.random.random((3,4))
print(data)

np.savetxt("../result/random_data.txt", data, delimiter=",")

data = np.loadtxt("../result/random_data.txt", delimiter = "")
print(data)
'''

