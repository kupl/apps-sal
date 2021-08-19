def round_to_next5(n):
    # Your code here
    if n == 0:
        return 0
    elif n % 5 == 0:
        return n
    else:
        return round_to_next5(n + 1)
