# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

## Check every combination of 2 values  summs to our target
##  n * n time complexity (n^2)

## A better way to solve it would be to use a hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index
        
        ## Iterate through every value in the array, get index and actual number
        for i, n in enumerate(nums):
          ## Check if the difference is already in the hashmap
            diff = target - n
            ## If it is, return the solution which is a pair of indices
            if diff in prevMap:
                return [prevMap[diff], i]
            ## If we don't find the solution, update hashmap and set the index = i
            prevMap[n] = i
        return


    