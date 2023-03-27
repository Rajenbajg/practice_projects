import numpy as np


# a =np.array([1,2,3,4,5])
# print(a)
# print(type(a))


# a[2]=10
# print(a)


###create multi dimensional array
# a_mul = np.array([[1,2,3],
#                  [4,5,6],
#                  [7,8,9]]
#                  )
# print(a_mul[0])
# print(a_mul[0,1])
# print(a_mul.shape)
# print(a_mul.ndim)
# print(a_mul.size)

#create array with same elements
a = np.full((2,3,4),9)
# print(a.ndim)

zero = np.zeros(a.shape)
print (zero)




