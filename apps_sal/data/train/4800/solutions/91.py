def hotpo(n):
    """
    Proof? Save that stuff for happy hour!
    """
    count = 0
    while n != 1:
        n = 3 * n + 1 if n % 2 else n // 2
        count += 1
    return count
