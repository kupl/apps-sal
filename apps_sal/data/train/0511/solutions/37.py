N = int(input())
A = [int(a) for a in input().split()]

total = 0
for a in A:
    total ^= a

for a in A:
    print(total ^ a, end=" ")
