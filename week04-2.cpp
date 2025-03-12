# week 04-2.c 是今天的Leetcode挑戰題 Easy
# Leetcode 2529.
#找出有幾個正數,有幾個負數
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0 #迴圈前面, 準備好,都放0
        for i in range(len(nums)): #迴圈中間,更新它
            if nums[i] > 0: pos +=1
            if nums[i] < 0: neg +=1
        #迴圈後面,把它拿來用
        return max(pos,neg)
