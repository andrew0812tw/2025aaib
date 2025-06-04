# week16-1.py
# 3403. Find the Lexicographically Largest String From the Box I
# ��r��fu, ����n�q, �Ҧ��i����k��,�r����̤j���p�r��^��
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1: return word #�N�u��1�q,���W�Y�i
        N = len(word) #�r�ꪺ����, �|�M�w�j��i �q���̶}�l
        M = N -(numFriends - 1)
        # �̱`�i�઺�r�ꪺ����: N - (n-1) ��L(n-1)��1�r��
        ans = word[0:M] #�̥���̪������Ӧr��
        for i in range(N): # �C�ӥi�઺�}�l����l i
            ans =  max(ans,word[i:i+M]) #�q i �}�l,�̪����r��,�O�_��j
        return ans
