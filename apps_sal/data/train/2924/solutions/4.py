def are_coprime(n, m):

    def factors(n):
        return [i for i in range(1, n + 1) if n % i == 0]
    return sorted(set(factors(n)) & set(factors(m)))[-1] == 1
