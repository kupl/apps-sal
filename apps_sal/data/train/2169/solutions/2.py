from collections import Counter
import sys
input = sys.stdin.readline

n, p, k = list(map(int, input().split()))
A = list(map(int, input().split()))

B = [(a**4 - k * a) % p for a in A]

C = Counter(B)


print(sum([l * (l - 1) // 2 for l in list(C.values())]))
