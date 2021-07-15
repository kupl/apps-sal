N, L = map(int, input().split())
ans = [input() for i in range(N)]
ans.sort()
ans = ''.join(ans)
print(ans)
