A = input()
N = len(A)
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alp_to_n = {}
for i, l in enumerate(alphabet):
    alp_to_n[l] = i

D = [True] * 26
L = [N]
s = 0
for i in range(N)[::-1]:
    if D[alp_to_n[A[i]]]:
        D[alp_to_n[A[i]]] = False
        s += 1
    if s == 26:
        D = [True] * 26
        L.append(i)
        s = 0
L.reverse()
ans = []
D = [True] * 26
for i in range(0, L[0]):
    D[alp_to_n[A[i]]] = False

for i in range(len(L) - 1):
    num, pos = 26, 0
    for j in range(L[i], L[i + 1]):
        if alp_to_n[A[j]] < num and D[alp_to_n[A[j]]]:
            num = alp_to_n[A[j]]
            pos = j
    ans.append(alphabet[num])
    D = [True] * 26
    for j in range(pos + 1, L[i + 1]):
        D[alp_to_n[A[j]]] = False
for i in range(26):
    if D[i]:
        ans.append(alphabet[i])
        break
print(("".join(ans)))
