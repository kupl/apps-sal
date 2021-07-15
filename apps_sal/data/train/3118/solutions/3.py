def is_lucky(n):
    return sum([int(i) for i in str(n)]) % 9 == 0
