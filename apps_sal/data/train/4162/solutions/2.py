def friends(n):
    return 0 if n < 2 else (n - 1).bit_length() - 1
