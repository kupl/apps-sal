n = int(input())
a = [0 for i in range(0, n + 1)]
b = [0 for i in range(0, n + 1)]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
dp = [0 for i in range(0, n + 1)]
c = [[0 for i in range(0, 3)] for j in range(0, n + 1)]
stack = []
stack.append(0)
stack.append(1)
dp[0] = 0
dp[1] = a[1] * b[0]


def intersection(x, y):
    return int((dp[y] - dp[x]) / (b[x] - b[y]))


last = 0
c[last] = [0, intersection(0, 1), 0]
last += 1
c[last] = [intersection(0, 1), 1000000001, 1]
last1 = 0
for i in range(2, n):
    while last1 >= 0:
        if c[last1][0] <= a[i] and c[last1][1] >= a[i]:
            dp[i] = dp[c[last1][2]] + b[c[last1][2]] * a[i]
            break
        elif c[last1][0] > a[i]:
            last1 -= 1
        else:
            last1 += 1
    while stack:
        top = stack[-1]
        if len(stack) >= 2:
            second_top = stack[-2]
            if intersection(second_top, i) < intersection(top, second_top):
                stack.pop()
                last -= 1
            else:
                break
        else:
            break
    stack.append(i)
    last += 1
    c[last] = [intersection(top, i), 1000000001, i]
    c[last - 1] = [c[last - 1][0], intersection(top, i), c[last - 1][2]]
print(dp[n - 1])
