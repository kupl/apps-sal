def part_const(n, k, num):
    return part(n, k) - part(n-(num or n), k-1)

def part(n, k):
    return 1 if k in (1, n) else sum(part(n-k, i) for i in range(1, min(n-k, k)+1))
