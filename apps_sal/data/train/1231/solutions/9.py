N = int(input())
for i in range(N):
    res = str(2 ** int(input()))
    ans = 0
    for i in res:
        ans += ord(i) - ord('0')
    print(ans)
