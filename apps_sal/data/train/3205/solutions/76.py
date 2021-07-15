def is_divisible(n,x,y):
    """(^__^)"""
    count = n%x or n%y
    if count == 0:
        return True
    elif count != 0:
        return False
