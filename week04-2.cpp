# week 04-2.c �O���Ѫ�Leetcode�D���D Easy
# Leetcode 2529.
#��X���X�ӥ���,���X�ӭt��
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0 #�j��e��, �ǳƦn,����0
        for i in range(len(nums)): #�j�餤��,��s��
            if nums[i] > 0: pos +=1
            if nums[i] < 0: neg +=1
        #�j��᭱,�⥦���ӥ�
        return max(pos,neg)
