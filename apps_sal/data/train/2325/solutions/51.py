s = input()
t = input()
q = int(input())
C = [list(map(int, input().split())) for i in range(q)]

S = [0]
T = [0]
for i in range(len(s)):
    if s[i] == "A":
        S.append(1)
    else:
        S.append(2)
for i in range(1, len(S)):
    S[i] = (S[i - 1] + S[i]) % 3

for i in range(len(t)):
    if t[i] == "A":
        T.append(1)
    else:
        T.append(2)
for i in range(1, len(T)):
    T[i] = (T[i - 1] + T[i]) % 3

for i in range(q):
    ss = (S[C[i][1]] - S[C[i][0] - 1]) % 3
    tt = (T[C[i][3]] - T[C[i][2] - 1]) % 3
    print("YES" if ss == tt else "NO")
