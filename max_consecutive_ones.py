"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

def findMaxConsecutiveOnes(nums):
        counter = 0
        max_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                counter = 0
            elif nums[i] == 1 and counter == 0:
                counter += 1
            elif nums[i] == 1 and nums[i-1] == 1:
                counter += 1
                
            if counter > max_count:
                max_count = counter
        return max_count

print(findMaxConsecutiveOnes([1,0,1,1,0,1]))