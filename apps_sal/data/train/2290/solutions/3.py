from collections import deque
(H, W) = list(map(int, input().split()))
S = [input() for i in range(H)]
table = [[0] * (W - 1) for i in range(H - 1)]
for i in range(W - 1):
    for j in range(H - 1):
        table[j][i] = (int(S[j][i] == '#') + int(S[j + 1][i] == '#') + int(S[j][i + 1] == '#') + int(S[j + 1][i + 1] == '#') + 1) % 2


def get_rec(L):
    a = len(L)
    arr = L + [0]
    stack = deque()
    ans = -1
    for i in range(a + 1):
        if len(stack) == 0:
            stack.append((arr[i], i))
        elif stack[-1][0] < arr[i]:
            stack.append((arr[i], i))
        elif stack[-1][0] > arr[i]:
            while len(stack) != 0 and stack[-1][0] >= arr[i]:
                (x, y) = stack.pop()
                ans = max((x + 1) * (i - y + 1), ans)
            stack.append((arr[i], y))
    return ans


dp = [[0] * (W - 1) for i in range(H - 1)]
for i in range(W - 1):
    for j in range(H - 1):
        if j == 0:
            dp[0][i] = table[0][i]
            continue
        if table[j][i] == 1:
            dp[j][i] = dp[j - 1][i] + 1
ans = max(H, W)
for j in range(H - 1):
    ans = max(ans, get_rec(dp[j]))
print(ans)
