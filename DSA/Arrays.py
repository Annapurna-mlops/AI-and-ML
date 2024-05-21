"""Reverse an Array
   Example : [1,2,3,4,5] to [5,4,3,2,1]
"""
import numpy as np
array_test = [1,2,3,4,5] # here we are defining a list using square brackets that suports hetrogenous data types
reverse_array = array_test[::-1]
print("revered array: ",reverse_array)
print("Using reverse method: ")
""" For this 
    Time complexity will be O(n) : copying elements to a new array is a linear operation
    Auxiliary Space Complexity: O(n) - Additional space is used to store the new array"""
array_test.reverse()
print(array_test)
""" For this 
    Time complexity will be O(1) : copying elements to a new array is a linear operation
    Auxiliary Space Complexity: O(n) - Additional space is used to store the new array"""

np_array_test = np.array([1,2,3,4,5]); 
""" We can create multi dimensional array using numpy.
    Numpy arrays are specifically designed for numerical computations and provide various functionalities optimized for effecient array operatios.
    Performance: NumPy arrays are typically faster for numerical computations due to optimized C-based operations"""

print ("reverse an array using numpy :", np_array_test[::-1]) # Since we are not storing output value oprinal value will be as is


"""Maximum and minimum of an array using minimum number of comparisons.

   Can we Sorting? so that, after sorting I can get min = array[0] and max= array[-1].
   But issue with sorting is Time complexity is O(n log n) due to sorting algorithm
   
   Linear Search : Initialize values of min and max as minimum and maximum of the first two elements respectively. 
   Starting from 3rd, compare each element with max and min, and change max and min accordingly 
   (i.e., if the element is smaller than min then change min, else if the element is greater than max then change max,
     else ignore the element)
    Time Complexity: O(n)
    Auxiliary Space: O(1) as no extra space was needed.
    
    Tournament Method: The idea is to divide the array into two parts and compare the maximums and minimums of 
    the two parts to get the maximum and the minimum of the whole array.
    Time Complexity: O(n)
    Auxiliary Space: O(log n) as the stack space will be filled for the maximum height of the tree formed during recursive calls same as a binary tree
    """

mini = float('-inf') #Convert a string or number to a floating point number, if possible
print("min value:", mini)
print(-5>mini)

# Python program of above implementation

# structure is used to return two values from minMax()

class pair:
    def __init__(self):
        self.min = 0
        self.max = 0

def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()

    # If there is only one element then return it as min and max both
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax

    # If there are more than one elements, then initialize min
    # and max
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax

# Driver Code
if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)

"""
Find the Kth max and min elements of an array:
Given an array arr[] and an integer k where k is smaller than the size of the array,
 the task is to find the kth smallest element in the given array.
 It is given that all array elements are distinct.

"""
arr_1 = [7,10,300,20,40]
k=3
arr_1.sort()
print("Sorted array: ", arr_1)
print("{}th minimum, position value is: {}".format(k, arr_1[k-1]))
print("{}th maximum, position value is: {}".format(k, arr_1[-(k)]))   # for array back index starts from -1
# for this approch TIme Complexity is O(n) and Auxiliary Space is O(log n)

"""
 Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order without using sort method
"""