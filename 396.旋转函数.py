#
# @lc app=leetcode.cn id=396 lang=python3
#
# [396] 旋转函数
#

# @lc code=start
from numpy import inf


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        import numpy as np
        sum_ = sum(nums)
        f0 = sum([i * nums[i] for i in range(len(nums))])
        max_value = f0
        F = f0
        for i in range(1, len(nums)):
            F = F + sum_ - (len(nums)) * nums[len(nums)-i]
            if F > max_value:
                max_value = F
        return max_value
# @lc code=end