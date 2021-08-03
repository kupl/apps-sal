import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    s = input()
    q = int(input())
    t = list(map(int, input().split()))
    stack = []
    val = [-1 for i in range(len(s))]
    last_open = -1
    for i in range(len(s) - 2, -1, -1):
        if s[i] == ')':
            stack.append(i)
            val[i] = last_open
        else:
            if len(stack) != 0:
                val[i] = stack[-1]
                stack.pop()
                last_open = val[i]
            else:
                last_open = -1

    for i in range(q):
        if val[t[i] - 1] == -1:
            print(-1)
        else:
            print(val[t[i] - 1] + 1)
