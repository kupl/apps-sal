def is_lucky(n):
    x = 0
    for i in str(n):
        x = x + int(i)
    return True if x % 9 == 0 else False
