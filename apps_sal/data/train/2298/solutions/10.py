# f = open('input', 'r')
# n, t = map(int, f.readline().split())
# A = list(map(int, f.readline().split()))
n, t = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0
max_diff = 0
min_a = A[0]
for a in A:
    min_a = min(min_a, a)
    if (a - min_a) == max_diff:
        ans += 1
    elif (a - min_a) > max_diff:
        ans = 1
        max_diff = (a - min_a)
print(ans)

