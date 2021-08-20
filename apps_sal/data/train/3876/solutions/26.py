def find(n):
    if n > 30:
        full = n // 30
        half = n % 30
        sum = full * (full - 1) * 210
        for i in range(3, half + 1):
            if i % 3 == 0 or i % 5 == 0:
                sum += i + full * 30
        sum += 225 * full
        return sum
    else:
        sum = 0
        for i in range(3, n + 1):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
        return sum
