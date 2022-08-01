class Solution(object):
    def numIdenticalPairs(self, nums):
        counter = Counter(nums)
        res = 0
        for num in counter:
            res += counter[num]*(counter[num]-1)//2
        return res
        