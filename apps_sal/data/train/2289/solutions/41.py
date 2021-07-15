A = [ord(a)-97 for a in input()]
N = len(A)
X = [0] * 26
Y = [0] * (N + 2)
NE = [0] * N
R = [N] * 26
s = 0
t = 1
for i in range(N)[::-1]:
    a = A[i]
    if X[a] == 0:
        X[a] = 1
        s += 1
        if s == 26:
            s = 0
            X = [0] * 26
            t += 1
    Y[i] = t
    NE[i] = R[a]
    R[a] = i

ANS = []
ii = 0
for i, a in enumerate(A):
    if i == ii:
        for j in range(26):
            if Y[R[j]+1] < Y[i]:
                ANS.append(j)
                ii = R[j]+1
                break
    R[a] = NE[i]

print("".join([chr(a+97) for a in ANS]))
