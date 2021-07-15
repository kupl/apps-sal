n = int(input())
res = 1

piece = [1 for i in range(n+2)]
for i in range(2, n+2):
    if piece[i] != 1:
        continue
    for j in range(i+i, n+2, i):
        piece[j] = 2

for p in piece:
   res = max(p, res)
print(res)
print(" ".join(map(str, piece[2:])))

