class Solution(object):
    def maxProduct(self, nums):
        a = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                a.append((nums[i] - 1) * (nums[j] - 1))

        return max(a)