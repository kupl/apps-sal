def part_const(n, k, num):
    return part(n, k) - (part(n-num, k-1) if num else 0)

def part(n, k):
    return 0 if k > n else 1 if k in {1, n} else sum(part(n-k, i) for i in range(1, k+1))

