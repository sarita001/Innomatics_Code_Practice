class Solution(object):
    def countBits(self, n):
        return [(list(bin(i)).count('1')) for i in range(0, n+1)]