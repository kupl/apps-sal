def gap(g, m, n):
    prev = None
    for i in range(m if m % 2 else m + 1, n + 1, 2):
        isPrime = True
        for k in range(2, round(i**0.5) + 1):
            if i % k == 0:
                isPrime = False
                break
        if isPrime:
            if prev:
                if i - prev == g:
                    return [prev, i]
            prev = i
    return None
