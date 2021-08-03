N, L = map(int, input().split())
array = [str(input()) for i in range(N)]
array = sorted(array)
ans = ''
for j in array:
    ans = ans + j
print(ans)
