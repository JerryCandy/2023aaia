class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a=arr
        N=len(a)
        for i in range(N-1):
            d=a[1]-a[0]#基礎的距離
            if a[i+1] - a[i] != d: #距離不相等
                return False

        return True