n = int(input())
li = list(map(int, input().split()))
m = int(input())
for i in range(m):
    l, r = list(map(int, input().split()))
    temp = li[l - 1:r]
    temp.sort()
    ans = 0
    for j in range(1, len(temp)):
        ans += (temp[j] - temp[j - 1])**2
    print(ans)
