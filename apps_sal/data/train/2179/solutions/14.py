a,b,c = list(map(int, input().split()))
n = int(input())
ans = 0
L = list(map(int, input().split()))
for i in L:
    if b < i < c:
        ans += 1
print(ans)

