def proper_fractions(n):
    factors = set()
    i = 2
    input = n
    while i * i <= input:
        if input % i == 0:
            factors.add(i)
            input = input // i
        else:
            i = i + 1
    factors.add(input)
    result = n
    for j in factors:
        result = result * (1 - 1 / j)
    return int(result)
