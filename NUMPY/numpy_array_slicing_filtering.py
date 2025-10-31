"""
NumPy Array Slicing & Filtering Demo
Author: Rajesh K
Description:
Demonstrates slicing, memory sharing, filtering, boolean indexing,
value replacement, and logical operations in NumPy.
"""

import numpy as np

#Slicing array
arr_10 = np.arange(start=10,stop=30,step=3)
print("\n arr_10 =", arr_10)

print("\n arr_10[2:6:2] =",arr_10[2:6:2]) #[START_index:STOP_index-1:STEP] 

print("\n arr_10[2:] =",arr_10[2:])

print("\n arr_10[:4] =",arr_10[:4])

print("\n arr_10[:-2] =",arr_10[:-2])

print("\n Last element in arr_10 =",arr_10[-1])

print("\n Reverse arr_10 =",arr_10[::-1])

print("\n arr_10[::2] =",arr_10[::2])

# Passing array value to another value 
arr_11 = arr_10[::2]    #Creates view to lookup value in arr_10 instead using new memory space to store values again

print("\n arr_11 =",arr_11)
      
print("\n Is arr_10 and arr_11 use same memory:",np.shares_memory(arr_10,arr_11)) 

print("\n Before changing arr_11, arr_10= ",arr_10)

arr_11[0] = 99

print("\n After changing arr_11, arr_10= ",arr_10)

arr_12 = arr_10[::2].copy()    #Use new memory space to store value

print("\n arr_12 =",arr_12)

print("\n Is arr_10 and arr_12 use same memory:",np.shares_memory(arr_10,arr_12))

print("\n Before changing arr_12, arr_10= ",arr_10)

arr_12[0] = 11

print("\n After changing arr_12, arr_10= ",arr_10)


#Create an number of random number between given number
arr_13 = np.random.randint(low=10,high=30,size=10)
print("\n arr_13 =",arr_13)

even_filter = (arr_13 % 2 == 0)

print("\n even_filter =",even_filter)

print("\n arr_13[even_filter] = ",arr_13[even_filter])

print("\n arr_13[arr_13 % 2 == 0] = ",arr_13[arr_13 % 2 == 0])

arr_13[arr_13 % 2 == 0] = -1 # assign -1 to all even number

print("\n Replaced even number arr_13 = ", arr_13)

# Change value at index level
arr_13[[0,3,5,7]] = 99
print("\n After change value at index [0,3,5,7], arr_13 =",arr_13)

arr_14 = np.arange(10)
print("\n arr_14 =",arr_14)

arr_14[3:5] = arr_13[3:5]

print("\n After assigning arr_13[3:5] to arr_14[3:5], arr_14 =",arr_14)

#Compare elements in the array
arr_18 = np.array([1,4,6,3])
print("\n arr_18 = ",arr_18)

arr_19 = np.array([1,2,6,4])
print("\n arr_19 = ",arr_19)

print("\n arr_18 == arr_19 => ",arr_18 == arr_19)

print("\n arr_18 > arr_19 => ",arr_18 > arr_19)

print("\n arr_18 < arr_19 => ",arr_18 < arr_19)

#Compare whole array
print("\n np.array_equal(arr_18,arr_19) => ",np.array_equal(arr_18,arr_19))

print("\n np.array_equal(arr_18,arr_18) => ",np.array_equal(arr_18,arr_18))

#Logical "or", "and" 
arr_19 = np.array([1,0,0,1,0],dtype=bool)
print("\n arr_19 = ",arr_19)

arr_20 = np.array([1,0,1,0,1],dtype=bool)
print("\n arr_20 = ",arr_20)

print("\n np.logical_and(arr_19,arr_20) => ",np.logical_and(arr_19,arr_20))

print("\n np.logical_or(arr_19,arr_20) => ",np.logical_or(arr_19,arr_20))
