"""
http://www.codechef.com/MAY14/problems/RRSTONE
"""
(N, K) = list(map(int, input().split()))
A = list(map(int, input().split()))
for i in range(min(K, K % 2 + 2)):
    m = max(A)
    A = [m - j for j in A]
print(' '.join(map(str, A)))
