#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ##  判断首行或者首列是否有0
        flag_r = False
        flag_l = False
        if 0 in matrix[0]:
            flag_r = True
        if 0 in [x[0] for x in matrix]:
            flag_l = True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0 for j in range(len(matrix[0]))]
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        if flag_r:
            matrix[0] = [0 for i in range(len(matrix[0]))]
        if flag_l:
            for i in range(len(matrix)):
                matrix[i][0] = 0

# @lc code=end

