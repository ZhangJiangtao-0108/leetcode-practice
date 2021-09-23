#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#

# @lc code=start
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = 0
        for i in range(len(nums)):
            nums_sum += nums[i]
        if nums_sum % k != 0:
            return False
        else:
            ave = nums_sum / k
            if max(nums) > ave:
                return False
            else:
                nums = sorted(nums,reverse=True)
                print(nums)
                nums_state = [0 for i in range(len(nums))]
                m = 0
                for i in range(len(nums)):
                    if nums_state[i] == 0 and self.f(0, nums, nums_state, i, ave):
                        m += 1
        return m==k
    def f(self, count, nums, nums_state, j, ave):
        if j ==len(nums) and count != ave or (count > ave):
            return False
        if count ==ave :
            return True
        for i in range(j, len(nums)):
            if nums_state[i] == 0:
                count += nums[i]
                nums_state[i]=1
                if self.f(count, nums, nums_state, i+1, ave):
                    return True
                count -= nums[i]
                nums_state[i] = 0
        return False
        
        
# @lc code=end

