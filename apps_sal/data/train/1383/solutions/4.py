import atexit
import io
import sys
import math
from collections import defaultdict, Counter

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

# dp=[0]*(2*pow(10,7)+1)
# for i in range(1,2*pow(10,7)+1):
#     d=int(math.sqrt(i))
#     if d*d==i:
#         c=0
#         for j in range(2,int(math.sqrt(d))+1):
#             if d%j==0:
#                 c=1
#                 break

#         if c==0:
#             dp[i]=3
#         else:
#             dp[i]=0
#     else:
#         dp[i]=1

# n0=[0]*(2*pow(10,7)+1)
# n1=[0]*(2*pow(10,7)+1)
# n3=[0]*(2*pow(10,7)+1)
# for i in range(1,2*pow(10,7)+1):
#     if dp[i]==0:
#         n0[i]=1
#     elif dp[i]==1:
#         n1[i]=1
#     else:
#         n3[i]=1
#     n0[i]+=n0[i-1]
#     n1[i]+=n1[i-1]
#     n3[i]+=n3[i-1]


def isprime(d):
    for j in range(2, int(math.sqrt(d)) + 1):
        if d % j == 0:
            return False
    return True


m = 100000007
t = int(input())
for i in range(t):
    n, k1, k2 = list(map(int, input().split()))
    p1, p2, p3, p4 = list(map(int, input().split()))
    p = int(math.sqrt(k1))
    if p * p < k1:
        p += 1
    c = 0
    ans = 0
    while p * p <= k2:
        c += 1
        if isprime(p):
            ans = (ans + p1) % m
        else:
            ans = (ans + p2) % m
        p += 1
    ans = (ans + (p3 * (k2 - k1 + 1 - c)) % m) % m
    print(ans)
