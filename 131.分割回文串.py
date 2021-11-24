#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def huiwen(str):
            if str == str[:,-1]:
                return True
            else:
                return False
        
        str_huiwen = []
        head, tial, step = 0, 0, 1
        while step < len(s):
            head, tial = 0, 0
            str_huiwen_sub = []
            while head < len(s):
                tial = head + step
                if tial < len(s):
                    if huiwen(s[head:tial]):
                        str_huiwen_sub.append(s[head:tial])
                        head = tial
                    else:
                        str_huiwen_sub.append(s[head])
                        head = head + 1
                else:
                    str_huiwen_sub
                


# @lc code=end

