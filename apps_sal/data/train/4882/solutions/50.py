def round_to_next5(n, base=5):
    # Your code here
    if n % 10 != 0:
        if n % 5 < 3:
            n += 2
        return base * round(n / base)
    return n
