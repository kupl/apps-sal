def are_coprime(n, m):
    num_of_n = [i for i in range(1, n + 1) if n % i == 0]
    for i in range(1, m + 1):
        if m % i == 0:
            if i in num_of_n[1:]:
                return False
    return True
