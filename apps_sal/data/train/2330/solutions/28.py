S = input()
T = S[:-1]

if S[0] == "0" or S[-1] == '1' or T != T[::-1]:
    print(-1)
    return

u = 1
for v in range(2, len(S) + 1):
    print(u, v)
    if S[v - 2] == '1':
        u = v
