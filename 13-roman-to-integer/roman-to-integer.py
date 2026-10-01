class Solution(object):
    def romanToInt(self, s):
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        sum = 0
        next = 0

        for i in reversed(s):
            current = values[i]

            if current < next:
                sum = sum - current
            else:
                sum = sum + current

            next = current

        return sum