def comp(a, b):
    try:
        return sorted(i*i for i in a) == sorted(b)
    except:
        return False
