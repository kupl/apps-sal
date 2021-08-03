m = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))

B_idx = sorted([(v, i) for (i, v) in enumerate(B)], reverse=True)
for i in range(m):
    B[B_idx[i][1]] = A[i]
print(" ".join([str(v) for v in B]))
