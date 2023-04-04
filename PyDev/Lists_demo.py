class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        count=0
        self.low=low
        self.high=high
        for i in range(low,high):
            if i%2!=0:
                count=count+1
        print(count)
obj =Solution()
obj.countOdds(3,7)
