def remove(s):
    return __import__('re').sub(r'\b!+','',s)
