def subsets(nums):
    result = []
    n = len(nums)
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                subset.append(nums[j])
        result.append(subset)
    return result
nums = [1,2,3]
print(subsets(nums))
nums = [0]
print(subsets(nums))
