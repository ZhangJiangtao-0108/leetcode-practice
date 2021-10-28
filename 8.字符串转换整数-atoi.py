#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        number = ['0','1','2','3','4','5','6','7','8','9']
        symber = ['+','-']
        string = s.lstrip()
        # i = 0
        # for i in range(len(s)):
        #     if s[i] != ' ':
        #         break
        #     else:
        #         string =string.replace(' ','',1)
        if string == "":
            return 0
        if string[0] not in (number + symber):
            return 0
        number_st = string[0]
        for i in range(1,len(string)):
            if string[i] in number:
                number_st += string[i]
            else:
                break
        if number_st in symber:
            return 0
        else:
            if int(number_st)< pow(-2,31):
                return pow(-2,31)
            elif int(number_st)>(pow(2,31) -1):
                return pow(2,31) -1
            else:
                return int(number_st)
            
# @lc code=end
    
