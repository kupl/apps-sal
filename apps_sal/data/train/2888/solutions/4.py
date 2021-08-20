def remove(s):
    return __import__('re').sub('\\b!+', '', s)
