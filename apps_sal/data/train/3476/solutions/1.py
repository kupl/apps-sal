def unlucky_number(n):
    return sum(1 for k in range(0, n+1, 13) if not set(str(k)) & {"4", "7"})

