def is_digit(n):
    print(n)
    try:
        return 0 <= int(n) < 10 if ''.join(n.split()) == n else False
    except:
        return False
