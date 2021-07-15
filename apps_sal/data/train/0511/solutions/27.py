from functools import reduce

N = int(input())
A = list(map(int, input().split()))

B = reduce(lambda x, y: x^y, A)

ans = []
for a in A:
    ans.append(B^a)

print(*ans)
