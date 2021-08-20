import atexit
import io
import sys
import math
from collections import defaultdict, Counter
t = int(input())
for i in range(t):
    (m, c, h) = map(int, input().split())
    if (h - c) % 3 == 0 and (h - c) // 3 <= m:
        print('No')
    else:
        print('Yes')
