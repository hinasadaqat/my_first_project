#Input: nums = [3,2,4], target = 6 Output: [1,2]
#find two number which sum give 6 value
# Two Sum Problem

nums = [3, 2, 4]
target = 6

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])