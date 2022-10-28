# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
from typing import List

class Solution(object):
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            nums[i] +=nums[i-1]
        return nums
nums = [1,2,3,4]
so = Solution()
print(Solution().runningSum(nums))