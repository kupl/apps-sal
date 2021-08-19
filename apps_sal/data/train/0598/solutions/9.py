"""
http://www.codechef.com/MAY14/problems/RRSTONE
"""

N, K = list(map(int, input().split()))
# print N,K
A = list(map(int, input().split()))
# print A

for i in range(min(K, K % 2 + 2)):
    m = max(A)
    A = [m - j for j in A]
    # print A

print(" ".join(map(str, A)))
