#
# @lc app=leetcode.cn id=29 lang=python3
#
# [29] 两数相除
#

# @lc code=start
from typing import Pattern


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pattern = '^[\-\+]?\d+'
        out = max(pow(-2,31),min(pow(2,31)-1, dividend/divisor))
        if out == pow(2,31)-1:
            return out
        else:
            out = str(out)
            # print(*re.findall(pattern, out))
            return int(*re.findall(pattern, out))
# @lc code=end

