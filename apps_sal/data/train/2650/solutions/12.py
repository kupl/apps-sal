(N, L) = input().split()
(N, L) = (int(N), int(L))
S = []
count = 0
while count < N:
    str = input()
    S.append(str)
    count += 1
S_ord = sorted(S)
print(''.join(S_ord))
