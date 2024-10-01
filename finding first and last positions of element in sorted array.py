def find_first_and_last(nums, target):
    def find_index(is_first):
        left, right = 0, len(nums) - 1
        index = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                index = mid
                if is_first:
                    right = mid - 1  
                else:
                    left = mid + 1   
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return index

    first_index = find_index(True)
    last_index = find_index(False)

    return [first_index, last_index]


nums = [5, 7, 7, 8, 8, 10]
target = 8
output = find_first_and_last(nums, target)
print(output)  

nums = [5, 7, 7, 8, 8, 10]
target = 6
output = find_first_and_last(nums, target)
print(output)  

nums = [5, 7, 7, 8, 8, 10]
target = 0
output = find_first_and_last(nums, target)
print(output)  