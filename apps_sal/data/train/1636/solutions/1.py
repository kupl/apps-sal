def prodsum(prod, sum_, fact, start):
    k = prod - sum_ + fact
    if k < n:
        if prod < mins[k]: mins[k] = prod
        for f in range(start, n // prod + 1):
            prodsum(prod * f, sum_ + f, fact + 1, f)

n = 100_000
mins = [2*k for k in range(n)]
prodsum(1, 1, 1, 2)
unique, sums = {0}, [0, 0]
for i in range(2, len(mins)):
    sums.append(sums[-1])
    if mins[i] not in unique:
        sums[-1] += mins[i]
        unique.add(mins[i])

productsum = sums.__getitem__
