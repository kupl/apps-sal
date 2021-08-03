S = input()
N = len(S)

if S[0] == "0":
    print("-1")
    return
if S[-1] == "1":
    print("-1")
    return

for s, rev_s in zip(S, reversed(S[:-1])):
    if s != rev_s:
        print("-1")
        return

prev = N

for i in reversed(list(range(1, N))):
    print((i, prev))
    if S[i - 1] == "1":
        prev = i
