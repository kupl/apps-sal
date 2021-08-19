import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
all = 0
for a_i in A:
    all ^= a_i
ans = []
for a_i in A:
    ans.append(all ^ a_i)
print(*ans)
