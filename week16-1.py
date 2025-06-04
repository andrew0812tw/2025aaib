# week16-1.py
# 3403. Find the Lexicographically Largest String From the Box I
# р﹃fu, ちΘn琿, ┮Τち猭い,ㄥ尿程﹃肚
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1: return word #碞だ1琿,
        N = len(word) #﹃, 穦∕﹚癹伴i 眖柑秨﹍
        M = N -(numFriends - 1)
        # 程盽﹃: N - (n-1) ㄤ(n-1)常1ダ
        ans = word[0:M] #程オ娩程êダ
        for i in range(N): # –秨﹍ i
            ans =  max(ans,word[i:i+M]) #眖 i 秨﹍,程﹃,琌
        return ans
