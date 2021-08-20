lens = int(input())
arrs = [int(x) for x in input().split()]
vals = []
for a in arrs:
    if a != 2:
        vals.append(2 ^ a)
    else:
        vals.append(3 ^ a)
print(*vals)
