class Solution:
    def isHappy(self, n: int) -> bool:
        n2 = 0
        while True :
            for i in str(n) :
                n2 += int(i)*int(i)
            n,n2=n2,0
            if n == 1 :
                return True
            elif n == 4 :
                return False


        