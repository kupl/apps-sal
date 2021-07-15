mod = 10**9+7
summ = 0
N = int(input())
for _ in range(N):
    a,b = map(int,input().split())
    summ+= (b-a)+1
print(summ%mod)
