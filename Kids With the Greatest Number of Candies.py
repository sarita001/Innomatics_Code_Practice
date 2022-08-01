class Solution(object):
    def kidsWithCandies(self,candies, extraCandies):
        m=0
        e=extraCandies
        l=[]
        for i in range(len(candies)):
            m=max(m,candies[i])
        for j in range(len(candies)):
            if (candies[j]+e)>=m:
                l.append(True)
            else : l.append(False)
        return l
            