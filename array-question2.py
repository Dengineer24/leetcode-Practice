# Given an array nums of integers, return how many of them contain an even number of digits

def evenDigits(nums, n):
    count = 0
    for i in range(0, n):
        allNumbs = nums[i]
        digit_value = len(str(allNumbs))
        if int(digit_value) % 2 == 0:
            count += 1
    return count

nums = [12,345,2,6,7896]
n = len(nums)

print(evenDigits(nums, n))