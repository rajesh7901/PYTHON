import numpy as np
import timeit as t 

l = [1, 2, 3, 4 ]
print('\n Python list - ',l)


a = np.array(l)
print('\n NumPy array - ',a)


arr = np.arange(100)
arr_time_taken = t.timeit ('arr** 2', globals=globals(), number=1000)
print( '\n time taken for numpy arr operation = ', arr_time_taken)
print('\n numpy arr used for above operation =', arr)

list_1 = list(range(100))
print(list_1)
list_time_taken = t.timeit ('[ i** 2 for i in list_1]', globals=globals(), number=1000)
print( '\n time taken for python list operation= ', list_time_taken)


arr_1 = np.arange(10)
print("\nNumpy Array arr_1 : ",arr_1) #Vector
print("Number of dimension: ", arr_1.ndim)
print("Shape of Array: ", arr_1.shape)
print("Size of Array: ", arr_1.size)


arr_2 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]]
                )

print("\nNumpy Matrix arr_2 : \n",arr_2)      #Matrix
print("Number of dimension: ", arr_2.ndim)
print("Shape of Array: ", arr_2.shape)
print("Size of Array: ", arr_2.size)

arr_3 = np.array([
                  [[1,2,3], [4,5,6]  ],
                  [[7,8,9],[10,11,12]]
                 ]
                )

print("\nNumpy 3D Matrix arr_3 : \n",arr_3)         #Tensor
print("Number of dimension: ", arr_3.ndim)
print("Shape of Array: ", arr_3.shape)
print("Size of Array: ", arr_3.size)


arr_4 = np.arange(start=2,stop=10,step=2)
print("\n arange arr_4 = ",arr_4)

arr_5 = np.linspace(start=2, stop=10, num=6 ) # (stop-start)/(n-1)gap b/w num =>   (10-2)/(6-1) => diff = 1.6  
print("\n linspace arr_5 =",arr_5)

arr_6 = np.ones((3,2))
print("\n Ones Matrix arr_6 =\n",arr_6)

arr_7 = np.zeros((3,3))
print("\n Zeros Matrix arr_7 =\n",arr_7)

arr_8 = np.eye(N=3,M=4,k=1)          # used to build an identity matrix (Diagonals are 1 and 0 everywhere) 
print("\n Identity Matrix arr_8 =\n",arr_8)

arr_9 = np.diag([1,2,3,4])
print("\n Diagonal Matrix arr_9 =\n",arr_9)

diagonal_element_arr_2 = np.diag(arr_2) # To fetch diagonal elements from an Matrix
print("\n Diagonal elements in arr_2 =",diagonal_element_arr_2)

random_arr_1 = np.random.rand(5)       #Uniform distributed random number b/w (0,1)
print("\n random_arr_1 = ",random_arr_1)

random_arr_2 = np.random.randn(4)      #standard normal distributed random number b/w(−inf,+inf) mean = 0, standard deviation = 1
print("\n random_arr_2 = ",random_arr_2)

print("\n arr_4 = ",arr_4,"| dtype = ",arr_4.dtype )

print("\n arr_5 = ",arr_5,"| dtype = ",arr_5.dtype )

complex_dtype_arr = np.array([1+2j,1+3j])
print("\n complex_dtype_arr = ",complex_dtype_arr,"| dtype = ",complex_dtype_arr.dtype )

bool_dtype_arr = np.array([True, False])
print("\n bool_dtype_arr = ",bool_dtype_arr,"| dtype = ",bool_dtype_arr.dtype )

str_dtype_arr = np.array(['Rajesh', 'Ram', 'Rakesh'],dtype='S')
print("\n str_dtype_arr = ",str_dtype_arr,"| dtype = ",str_dtype_arr.dtype )
