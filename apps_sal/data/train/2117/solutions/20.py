

n = int(input().strip())
a = list(map(int, input().strip().split()))

ans = [0] * (n + 1)

a = [0] + a + [0]
s = []

for index, value in enumerate(a):
    while s and value < s[-1][0]:
        ans[index - s[-2][1] - 1] = max(s[-1][0], ans[index - s[-2][1] - 1])
        s.pop()
    s.append((value, index))


ans = ans[::-1]
for i in range(n):
    ans[i + 1] = max(ans[i + 1], ans[i])
ans = ans[::-1]
print(' '.join(map(str, ans[1:])))


"""

10
1 2 3 4 5 4 3 2 1 6

3
524125987 923264237 374288891

"""
