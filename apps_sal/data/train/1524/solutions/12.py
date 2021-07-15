t = eval(input())

for _ in range(t):
 n, k = list(map(int, input().split()))
 ans = k*((k-1)**(n-1))
 print(ans%1000000007)
