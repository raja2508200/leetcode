class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        l=[0,1]
        for i in range(2,n+1):
            c=a+b
            a=b
            b=c
            l.append(c)
        return l[n]
                