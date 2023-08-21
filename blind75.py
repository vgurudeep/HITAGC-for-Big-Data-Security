# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.

# input - [2,3,4,1] - target = 6, output = [0,2]
# class Solution(object):
def twoSum(nums, target):
    sol = []
    for i in nums:
        num1 = i
        if nums.index(target - num1):
            sol.append(nums.index(target-num1))
            sol.append(nums.index(num1))
    return sol
nums = [3, 3]
target = 6

print(twoSum(nums, target))
