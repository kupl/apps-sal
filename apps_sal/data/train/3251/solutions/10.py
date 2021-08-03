from itertools import compress


def sieve(n):
    out = [True] * ((n - 2) // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if out[(i - 3) // 2]:
            out[(i**2 - 3) // 2::i] = [False] * ((n - i**2 - 1) // (2 * i) + 1)
    return [2] + list(compress(range(3, n, 2), out))


def primeFactors(n):
    str_lst = []
    for i in sieve(int(n**0.5) + 1):
        if n % i == 0:
            str_lst.extend(["(", str(i)])
            counter = 0
            while n % i == 0:
                n = n // i
                counter += 1
            if counter == 1:
                str_lst.append(")")
            else:
                str_lst.extend(["**", str(counter), ")"])
    if n != 1:
        str_lst.extend(["(", str(n), ")"])
    return "".join(str_lst)
