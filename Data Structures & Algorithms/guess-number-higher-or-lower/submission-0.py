# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

import random
class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        # random_number = random.randint(1, n)
        # guessed = guess(random_number)
        while l <= r:
            m = l + (r - l)//2
            guessed = guess(m)
            if guessed == -1:
                r = m - 1
            elif guessed == 1:
                l = m + 1
            else:
                return m
        return 