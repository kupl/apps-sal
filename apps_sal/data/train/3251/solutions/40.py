def primeFactors(n):
    i = 2
    a = []
    while i <= n:
        if n % i == 0:
            if not any([i % x[0] == 0 for x in a]):
                max_power = 0
                div = n
                while div % i == 0:
                    max_power += 1
                    div /= i
                a.append((i, max_power))
                n /= i
        i += 1
    return ''.join([f'({x}**{y})' if y != 1 else f'({x})' for (x, y) in a])
