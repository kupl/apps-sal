def gap(g, m, n):
    first = first_prime(m, n)
    while first:
        next = first_prime(first+1, n)
        if next is not None and (next - first == g):
            return [first, next]
        first = first_prime(first+1, n)
    return None

def first_prime(start, end):
    for num in range(start, end+1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            return num
    return None

