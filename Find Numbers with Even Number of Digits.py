class Solution:
    def findNumbers(self, nums):
        count_even = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count_even += 1
        return count_even