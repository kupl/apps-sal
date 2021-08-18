import numpy as np
import sys
N = int(input())
A = np.zeros(N, dtype=np.int64)
B = np.zeros(N, dtype=np.int64)
for i in range(N):
    A[i], B[i] = map(int, input().split())
if all(A == B):
    print(0)
    return
ans = A.sum() - B[A > B].min()
print(ans)
