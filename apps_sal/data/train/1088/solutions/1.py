for _ in range(int(input())):
 m, p = map(float, input().split())
 ans = 10**9 * (1 - (-p)**m) / (1 + p)
 print(ans,10**9-ans)
