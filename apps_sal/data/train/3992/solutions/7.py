def is_happy(n):
    lst = []
    while n != 1:
        n = sum((int(i) ** 2 for i in str(n)))
        if n in lst:
            return False
        lst.append(n)
    return True
