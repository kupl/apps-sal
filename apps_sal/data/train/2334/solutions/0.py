import sys
readline = sys.stdin.readline
T = int(readline())
Ans = [None] * T
for qu in range(T):
    S = [1 if s == 'A' else 0 for s in readline().strip()]
    stack = []
    for s in S:
        if s:
            stack.append(s)
        elif stack and stack[-1] == 1:
            stack.pop()
        else:
            stack.append(s)
    stack2 = []
    for s in stack:
        if s:
            stack2.append(s)
        elif stack2 and stack2[-1] == 0:
            stack2.pop()
        else:
            stack2.append(s)
    Ans[qu] = len(stack2)
print('\n'.join(map(str, Ans)))
