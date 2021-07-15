def is_digit(n):
    d="0123456789"
    if len(n)!=1:
        return False
    for i in n:
        if i in d:
            return True
            break
        else:
            return False
