def remove(s):
    return __import__('re').sub('!+(?!!*$)', '', s)
