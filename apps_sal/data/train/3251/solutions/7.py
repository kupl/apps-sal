def primeFactors(n):
    result = ""
    for k, v in factorize(n).items():
        result += f'({k})' if v == 1 else f'({k}**{v})'
    return result


def factorize(n):
    result, i = {}, 2
    while n >= i ** 2:
        if n % i == 0:
            result[i] = 1 if not result.__contains__(i) else result[i] + 1
            n = n // i
        else:
            i += 1
    result[n] = 1 if not result.__contains__(n) else result[n] + 1
    return result
