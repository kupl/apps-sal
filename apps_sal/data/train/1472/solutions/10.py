n = int(input().lstrip())


sn = 0
psn = 0

for i in range(1, 1000000):
    prod = 1
    for j in str(i):
        prod *= int(j)

    if prod == n:
        if "1" in str(i):
            psn += 1
        else:
            sn += 1

print(sn, psn)
