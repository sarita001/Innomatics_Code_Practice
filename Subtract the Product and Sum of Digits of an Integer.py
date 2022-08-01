class Solution(object):
    def subtractProductAndSum(self, n):
        add = 0
        mul = 1
        while n >= 1:
            add += n % 10
            mul *= n % 10
            n = n // 10
            
        return mul-add
