# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# [-4,-1,0,3,10]
 
def sortSquare(nums, n):

    for i in range(n):
        nums[i] = nums[i] * nums[i]
    nums.sort()

    
nums = [-4,-1,0,3,10]
n = len(nums) 

sortSquare(nums, n)
 
for i in range(n):
    print(nums[i], end = " ")