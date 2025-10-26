import numpy as np

# תרגילים מאמצע העמוד
# תרגיל 1
rand_arr_between1_to50 = np.random.randint(1, 50, size = (10))
print(rand_arr_between1_to50.size)
print(rand_arr_between1_to50.dtype)
print(rand_arr_between1_to50.shape)

#תרגיל 2
arr = np.random.randint(10, 100, size = (2, 5))
print(arr)
print(arr.shape)

# תרגילים מסוף העמוד
# תרגיל 1
arr1 = np.random.randint(1, 50, size = 10)
avg = np.mean(arr1)
print(avg)

# תרגיל 3
arr2 = np.random.randint(1, 100, size = 20)
print(arr2)
condition = arr2 > 50
bigger50 = arr2[condition]
print(bigger50)