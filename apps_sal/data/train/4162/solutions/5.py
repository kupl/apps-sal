def relu(n):
    return 0 if n < 0 else n

def friends(n):
    return relu(~-(~-n).bit_length())
