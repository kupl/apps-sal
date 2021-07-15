import numpy as np

N,T = list(map(int,input().split()))

A = np.array(list(map(int,input().split())))

B = np.minimum.accumulate(A)

C = A - B

ans = (C == C.max()).sum()

print(ans)

