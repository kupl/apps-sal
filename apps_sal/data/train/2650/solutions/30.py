n, l = list(map(int, input().split()))

strList = []
for _ in range(0, n):
    strList.append(input())

strList.sort()

ans = ""
for i in range(0, n):
    ans += strList[i]

print(ans)
