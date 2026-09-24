# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         unique_index=0

#         for index, i in enumerate(nums):
#             if nums[index] != nums[index-1]:
#            unique_index=  unique_index + 1
#             nums[unique_index]=nums[index]
     
#      k = unique_index + 1 
#      return k
            
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique_index = 0

        # Start from index 1
        for index in range(1, len(nums)):

            # Compare current element with previous element
            if nums[index] != nums[index - 1]:

                unique_index = unique_index + 1

                nums[unique_index] = nums[index]

        # After loop is finished
        k = unique_index + 1

        return k