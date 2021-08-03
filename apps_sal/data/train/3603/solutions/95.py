def lovefunc(f1, f2):
    if f1 % 2 == 0 and f2 % 2 == 0:
        return False
    if f1 & 2 == 1 and f % 2 == 1:
        return False
    else:
        return True
