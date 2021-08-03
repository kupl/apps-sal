n, k = [int(c) for c in input().split()]
a = []
for i in range(k):
    ak = [int(c) for c in input().split()]
    a.append(ak[1:])

total = k - 1

for ak in a:
    if ak[0] == 1:
        j = 1
        while j <= len(ak) - 1:
            if ak[j] != ak[j - 1] + 1:
                break
            j += 1
        total += 2 * (len(ak) - j)
    else:
        total += 2 * (len(ak) - 1)

print(total)
