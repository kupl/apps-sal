def is_lucky(n):
    count = 0
    n = str(n)
    for i in n:
        count += int(i)
    if count == 0 or count % 9 == 0:
        return True
    return False
