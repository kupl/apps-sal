n = int(input())
ans = 0
stk = []
for v in map(int, input().split()):
    last = 0
    while len(stk) and stk[-1][0] < v and stk[-1][1]:
        last = max(last, stk[-1][1])
        del stk[-1]
    if not len(stk) or stk[-1][0] < v:
        stk.append((v, 0))
    else:
        stk.append((v, last + 1))
        ans = max(ans, last + 1)
print(ans)
