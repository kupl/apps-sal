def is_uppercase(inp):
    for I in inp:
#         print(ord(I))
        if ord(I)>=97 and ord(I)<=122:
            return False
    return True
