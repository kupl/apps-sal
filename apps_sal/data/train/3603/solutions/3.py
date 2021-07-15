def lovefunc(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return False
    elif a % 2 != 0 and b % 2 == 0:
        return True
    elif a % 2 == 0 and b % 2 != 0:
        return True
    else:
        return False
