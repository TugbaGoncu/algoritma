
#https://leetcode.com/problems/two-sum/
def twoSumTarget(nums, target):
    found = False
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f'{nums[i]}+{nums[j]}={target}')
                found = True
                break
        if found:
            break

nums = [1, 9, 8, 2, 3, 17, 5, 18]
target = 6
twoSumTarget(nums, target)
