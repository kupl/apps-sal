def gap(g, m, n):
    def is_prime(num):
        if num < 4: return num > 1
        if num % 6 != 1 and num % 6 != 5: return False
        sqrt = int(num ** 0.5)
        for i in range(5, sqrt + 1, 6):
            if num % i == 0 or num % (i + 2) == 0: return False
        return True

    for i in range(m, n + 1):
        if is_prime(i):
            for j in range(i + 1, n + 1):
                if is_prime(j):
                    if j - i == g:
                        return [i, j]
                    break
                if j == n: return None
    return None
