import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

N = ir()
A, B = np.array([lr() for _ in range(N)]).T
if np.all(A == B):
    print((0)); return

index = np.where(B<A)[0]
answer = np.sum(A) - np.min(B[index])
print(answer)

# 12

