#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ## 需要三个指针记录0，1，2的位置
        # p0 = 0
        # p1 = nums.count(0)
        # p2 = nums.count(0) + nums.count(1)
        # p0 = [0,nums.count(0), nums.count(0) + nums.count(1)]
        # p = [0,nums.count(0), nums.count(0) + nums.count(1)]
        # print(p)
        ## 从第0个位置开始遍历整个列表，进行位置替换
        # ind = 0
        # count = 0
        # while ind < len(nums):
            # nums[p[nums[ind]]], nums[ind] = nums[ind], nums[p[nums[ind]]]
            # temp = nums[p[nums[ind]]]
            # nums[p[nums[ind]]] = nums[ind]
            # print(nums[ind],p[nums[ind]]+1)
            # p[nums[ind]] = p[nums[ind]]+1
            
            # nums[ind] = temp
            # p[nums[ind]] = min(p[nums[ind]], p0[nums[ind]]+nums.count(nums[ind]))
            
            ## 参数更新
            # print('p0:',p0)
            # print('p:',p)
            # ind += 1
            # print(ind)
            # count += 1
            # print(count)
            # print('nums:',nums)
            
        p0, p2 = 0, len(nums)-1
        i = 0
        while i < (p2+1):
            if nums[i] == 2:
                nums[i], nums[p2] = nums[p2],nums[i]
                p2-=1
            elif nums[i] == 0:
                if i != p0:
                    nums[i], nums[p0] = nums[p0],nums[i]
                    p0 += 1
                else:
                    i += 1
            else:
                i += 1
            print(nums)
            
# @lc code=end

