class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index, i in enumerate(nums):
            required = target - i
            
            if required in nums:
                required_index = nums.index(required)
                if required_index != index:
                 return [index, required_index]