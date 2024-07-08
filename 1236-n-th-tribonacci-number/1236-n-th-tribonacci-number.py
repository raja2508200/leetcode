class Solution:
    def tribonacci(self, n: int) -> int:
        a=0
        b=1
        c=1
        l=[0,1,1]
        for i in range(3,n+1):
            d=a+b+c
            l.append(d)
            a=b
            b=c
            c=d
        return l[n]
            