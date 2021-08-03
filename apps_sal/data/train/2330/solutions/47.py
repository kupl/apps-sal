S = input()
if S[0] == "0" or S[-1] == "1":
    print((-1))
    return
n = len(S)
for i in range(n // 2):
    if S[i] != S[n - 2 - i]:
        print((-1))
        return

for i in range(2, n // 2 + 1):
    print((1, i))
bef = 1
for i in range(n // 2 + 1, n + 1):
    print((bef, i))
    if S[i - 2] == "1":
        bef = i
