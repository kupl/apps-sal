from bisect import bisect_right, bisect_left
A = [ord(t) - ord("a") for t in input()]
n = len(A)
alf = [[] for i in range(26)]
for i, a in enumerate(A):
    alf[a].append(i)
for i in range(26):
    alf[i].append(n + 1)

first = [n]
appeard = [0] * 26
cnt = 0
for i in range(n - 1, -1, -1):
    a = A[i]
    if 1 - appeard[a]:
        appeard[a] = 1
        cnt += 1
    if cnt == 26:
        first.append(i)
        cnt = 0
        appeard = [0] * 26


def ntoa(x):
    return chr(ord("a") + x)


first.reverse()
ans = ""

for i in range(26):
    if 1 - appeard[i]:
        ans += ntoa(i)
        if alf[i]:
            last = alf[i][0]
        break
if len(first) == 1:
    print(ans)
    return

for j in range(len(first) - 1):
    for i in range(26):
        nxt = alf[i][bisect_right(alf[i], last)]
        if nxt >= first[j + 1]:
            ans += ntoa(i)
            last = nxt
            break
print(ans)
