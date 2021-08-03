def round_to_next5(n):
    # Your code here
    return n if n % 10 == 0 else n + (-n % 5)
