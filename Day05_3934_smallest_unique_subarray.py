from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        for length in range(1, n + 1):
            count = {}

            for i in range(n - length + 1):
                subarray = tuple(nums[i:i + length])

                count[subarray] = count.get(subarray, 0) + 1

            for freq in count.values():
                if freq == 1:
                    return length
