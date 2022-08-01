class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        s = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if i != j:
                    if nums[i] > nums[j]:
                        count += 1
            s.append(count)
        return s