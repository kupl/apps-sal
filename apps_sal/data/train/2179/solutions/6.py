a, b, c = list(map(int, input().split()))
n = int(input())
a = [int(s) for s in input().split()]

ans = 0
for i in range(n):
    if a[i] > b and a[i] < c:
        ans += 1

print(ans)
