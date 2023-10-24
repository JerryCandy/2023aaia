class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: #負的數一定是錯的，0也是錯的
            return False
            
        while n>1 :
            if n%2 !=0 : #有餘數，就失敗了
                return False#失敗
            else:
                n=n // 2 #16//2得到8，數字變小

        return True