# Given a binary array nums, return the maximum number of consecutive 1's in the array.

def maxConsecutive(nums, n):
    count = 0
    result = 0 
    for i in range (0 , n):
        if (nums[i] == 0):
            count = 0
        else:
            count += 1 
            result = max(result, count)
    return result

nums = [1,1,0,1,1,1]
n = len(nums)
print(maxConsecutive(nums, n))