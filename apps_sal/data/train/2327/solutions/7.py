import sys
input = sys.stdin.readline
class BIT():
    def __init__(self, number):
        self.n = number
        self.list = [0] * (number + 1)

    def add(self, i, x):  # ith added x  1indexed
        while i <= self.n:
            self.list[i] += x
            i += i & -i

    def search(self, i):  # 1-i sum
        s = 0
        while i > 0:
            s += self.list[i]
            i -= i & -i
        return s

    def suma(self, i, j):  # i,i+1,..j sum
        return self.search(j) - self.search(i - 1)

N,M=list(map(int,input().split()))
L=[[] for i in range(M+1)]
bit=BIT(M+1)
for i in range(N):
    l,r=list(map(int,input().split()))
    L[r-l+1].append((l,r))
ans=N
for i in range(1,M+1):
    num=0
    for l,r in L[i]:
        ans-=1
        bit.add(l,1)
        bit.add(r+1,-1)
    num+=ans
    for j in range(i,M+1,i):
        num+=bit.search(j)
    print(num)

