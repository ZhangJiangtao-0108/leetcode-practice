#
# @lc app=leetcode.cn id=1345 lang=python3
#
# [1345] 跳跃游戏 IV
#

# @lc code=start


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        ## 统计路径
        path_dic = {}
        for i in range(len(arr)):
            if arr[i] in path_dic.keys():
                path_dic[arr[i]].append(i)
            else:
                path_dic[arr[i]] = [i]
        count = 0
        path = path_dic[arr[0]] + [1]
        if len(arr) == 1:
            flag = False
        else:
            flag = True
        path.remove(0)
        path_bool = [0 for k in range(len(arr))]
        path_bool[0] = 1
        while flag:
            print(path)
            path_ = []
            count += 1 
            if (len(arr) -1) in path:
                flag = False
            for j in path:
                path_bool[j] = 1
                if j-1 >= 0 and path_bool[j-1] == 0:
                    path_.append(j-1)
                if j + 1 < len(arr) and path_bool[j+1] == 0:
                    path_.append(j+1)
                for m in path_dic[arr[j]]:
                    if path_bool[m] == 0: 
                        path_.append(m) 
                path_dic[arr[j]] = []
            path = path_

        
        return count



# @lc code=end

