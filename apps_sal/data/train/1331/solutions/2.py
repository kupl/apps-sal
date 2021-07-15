from math import log, floor

T = int(input())
for _ in range(T):
 X, K = [int(x) for x in input().split()]
 
 k = floor(log(K, 2))
 x = 2 ** k
 
 print(X/ x * (0.5 + K - x))
