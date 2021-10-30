numbers = [1,4,9,10,5,7]
# not sorted 
target = 4

def binary_search(numbers, target):
    numbers.sort()
    left_i = 0
    right_i = len(numbers) - 1
    mid_i = 0

    while left_i <= right_i:
        mid_i = (left_i + right_i) // 2
        mid_num = numbers[mid_i]

        if mid_num == target:
            return mid_i

        if mid_num < target:
            left_i = mid_num + 1 
        
        else:
            right_i = mid_num - 1 

    return -1 

index = binary_search(numbers, target)
print(index)