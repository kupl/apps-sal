def primeFactors(n):
    power = {}
    div = 2
    while div <= n:
        if n % div == 0:
            if div in power:
                power[div] += 1
            else:
                power[div] = 1
            n /= div
        else:
            div += 1
    return ''.join([f"({k}**{v})" if v > 1 else f"({k})" for k, v in power.items()])
