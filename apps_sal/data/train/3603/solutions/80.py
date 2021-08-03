def lovefunc(f1, f2):
    if f1 % 2 == 0 and f2 % 2 != 0:
        return True
    if f2 % 2 == 0 and f1 % 2 != 0:
        return True
    else:
        return False
