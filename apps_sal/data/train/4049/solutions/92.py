def monkey_count(n):
    return [] if n < 1 else monkey_count(n-1) + [n]
