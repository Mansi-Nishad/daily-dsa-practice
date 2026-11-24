from math import gcd
from functools import reduce

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 1

        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]

                subarray = nums[i:j+1]
                g = reduce(gcd, subarray)
                l = reduce(lambda a, b: a * b // gcd(a, b), subarray)

                if product == g * l:
                    max_len = max(max_len, j - i + 1)

        return max_len
