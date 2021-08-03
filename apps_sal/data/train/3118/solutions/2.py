def is_lucky(n):
    digits = list(str(n))
    return sum(list(map(int, digits))) % 9 == 0
