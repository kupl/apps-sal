def unlucky_number(n):
    return sum((x % 13 == 0 and '4' not in str(x) and ('7' not in str(x)) for x in range(n + 1)))
