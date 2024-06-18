"""
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 9
"""
arr = [1,0,2,3,0,4,5,0]

def duplicateZeros(arr):
  # convert array of ints into a string
  arr_str = ' '.join(map(str, arr))

  # duplicate 0s and split str into a list
  arr_str = arr_str.replace('0', '0 0').split()

  # map list of str to a list of ints
  arr_str = list(map(int, arr_str))

  # modify arr in place
  for i in range(len(arr)):
    arr[i] = arr_str[i]

duplicateZeros(arr)
print(arr)