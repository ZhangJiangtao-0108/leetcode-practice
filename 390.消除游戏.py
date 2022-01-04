#
# @lc app=leetcode.cn id=390 lang=python3
#
# [390] 消除游戏
#

# @lc code=start
class Solution:
    def lastRemaining(self, n: int) -> int:
        arr = [i+1 for i in range(n)]
        while len(arr) > 1:
            arr = arr[1:len(arr):2]
            arr = arr[::-1]
        # print(arr[0])
        return arr[0]
# @lc code=end

