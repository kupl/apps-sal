def divisors(n):
    devisors = []
    for number in range(1, n + 1):
        result = n % number
        if result == 0:
            devisors.append(result)
    return len(devisors)
