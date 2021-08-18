import sys
import math
from collections import defaultdict, Counter


k, a, b = list(map(int, input().split()))
if b <= a + 2 or k <= a:
    ans = 1 + k
else:
    k -= a - 1
    ans = a + k // 2 * (b - a)
    if k & 1:
        ans += 1
print(ans)
