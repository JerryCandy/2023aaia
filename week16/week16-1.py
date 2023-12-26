class Solution:
    def maxScore(self, s: str) -> int:
        N = len(s)
        ans=0
        for left in range(N-1):
            now=0
            for i in range(N):
                if i<=left and s[i]=='0':now +=1 #左邊的0，成功
                if i>left and s[i]=='1':now +=1
            if now>ans: ans=now
        return ans