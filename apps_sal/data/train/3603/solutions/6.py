def lovefunc(f1, f2):
    return True if f1 % 2 == 0 and f2 % 2 != 0 or (f2 % 2 == 0 and f1 % 2 != 0) else False
