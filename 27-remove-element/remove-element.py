
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        count = 0

        for index, i in enumerate(nums):
            if i != val:
                nums[count] = i
                count = count + 1

        return count

# Initially, `count` is `0`.

# For example:

# `nums = [3, 2, 2, 3]`
# `val = 3`

# First, we check `3`.

# `3 == 3`, so we don't keep it.

# Next, we check `2`.

# `2 != 3`, so we want to keep `2`.

# Because `count` is initially `0`, we put `2` at the 0th index:

# `nums[count] = i`

# So:

# `nums[0] = 2`

# Then we increase `count` by 1:

# `count = count + 1`

# Now `count` becomes `1`, so the next valid value will be placed at index `1`.

# In simple words:

# **Put the valid value at the current `count` position, then increase `count` to move to the next position.**
