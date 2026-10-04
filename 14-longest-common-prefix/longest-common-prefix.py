class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        result = ""
        min_length = min(len(i) for i in strs)

        #  index  strs
        #   ↓
        # 0 → "flower"
        # 1 → "flow"
        # 2 → "flight"

        for index in range(min_length):
            char = strs[0][index]

            for i in strs:
                if i[index] != char:
                    return result

            result = result + char

        return result


# 1st loop = take one character position
# 2nd loop = check that position in every string
# 1st loop → position 0
# 2nd loop → check position 0 in all strings
# 1st loop → position 1
# 2nd loop → check position 1 in all strings
# i[index] = get the character at that position
# Example: i = "flower", index = 2 → i[index] = "o"