class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        sum = 0
        result = []

        for index, i in enumerate(nums):
              sum = sum + i
              result = result + [sum]

        return result

