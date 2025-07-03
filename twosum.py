class Solution:
    def twoSum(self, nums, target):
        seen = {}  # Dictionary to store number:index

        for index, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], index]
            seen[num] = index

