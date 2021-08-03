N = int(input())
A = [int(i) for i in input().split()]
total = 0
for a in A:
    total ^= a
print(*[total ^ a for a in A])
