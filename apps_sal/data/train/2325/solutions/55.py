import sys
input = sys.stdin.readline
S = list(input())[: -1]
T = list(input())[: -1]
css = [0] * (len(S) + 1)
cst = [0] * (len(T) + 1)

for i in range(len(S)):
    css[i + 1] = css[i] + (S[i] == "A") + (S[i] == "B") * 2
for i in range(len(T)):
    cst[i + 1] = cst[i] + (T[i] == "A") + (T[i] == "B") * 2


for _ in range(int(input())):
    a, b, u, v = map(int, input().split())
    if (css[b] - css[a - 1]) % 3 == (cst[v] - cst[u - 1]) % 3:
        print("YES")
    else:
        print("NO")
