class Solution(object):
    def xorOperation(self, n, start):
        num = 0
        st_num = start
        for i in range(1,n):
            num = start + 2 * i
            st_num ^= num
        return st_num