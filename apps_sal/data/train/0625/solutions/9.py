from collections import defaultdict
from itertools import accumulate
for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    K = 10**9
    ans, rems = 0, {0: 1}
    for i in range(len(A)):
        if i > 0:
            A[i] += A[i - 1]
        rem = A[i] % K
        if rem in rems:
            ans += rems[rem]
            rems[rem] += 1
        else:
            rems[rem] = 1
    print(ans)
