(n, q) = list(map(int, input().split()))
F = []
S = []
line1 = input().split()
last = 0
for i in range(n):
    F.append(int(line1[i]))
    last = last ^ int(line1[i])
    S.append(last)
S.append(0)
for i in range(q):
    query = int(input())
    pos = (query - 1) % len(S)
    final = S[pos]
    print(final)
