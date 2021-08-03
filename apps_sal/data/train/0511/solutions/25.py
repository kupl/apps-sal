input()
A = [*map(int, input().split())]
s = 0
for a in A:
    s ^= a
print(*[a ^ s for a in A])
