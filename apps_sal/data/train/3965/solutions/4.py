def powerof4(n):
    try:
        b = bin(n)
        if isinstance(n, bool):
            return False
        return b.count('1') == 1 and len(b) % 2 != 0
    except:
        return False
