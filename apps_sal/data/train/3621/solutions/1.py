def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_maxlength_chain(n):
    (summ, primes, res) = (0, [], [])
    for i in range(2, n):
        if is_prime(i):
            if summ + i < n:
                summ += i
                primes.append(i)
            elif summ + i - primes[0] < n:
                summ += i
                primes.append(i)
            else:
                break
    l = len(primes)
    for j in range(l, 0, -1):
        for k in range(l - j + 1):
            lst = primes[k:k + j]
            temp = sum(lst)
            if is_prime(temp):
                res.append(temp)
        if len(res) != 0:
            break
    return res
