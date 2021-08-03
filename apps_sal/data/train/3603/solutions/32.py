def lovefunc(f, f1):
    if f % 2 == 0 and f1 % 2 != 0:
        return True
    return True if f % 2 != 0 and f1 % 2 == 0 else False
