#Input: nums = [3,3], target = 6
Output: [0,1]
# Two Sum - Example 3

nums = [3, 3]
target = 6

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])