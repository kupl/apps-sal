_, *A = map(int, open(s := 0).read().split())
for a in A:
    s ^= a
print(*[a ^ s for a in A])
