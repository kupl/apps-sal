def remove(s):
    return __import__('re').sub(r'!+(?!!*$)', '', s)
