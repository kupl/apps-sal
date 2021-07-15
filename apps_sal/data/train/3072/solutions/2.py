def is_narcissistic(*arg):
    for e in arg:
        try:
            if e == 0:
                continue
            n = int(e) == sum([int(i) ** len(str(e)) for i in str(e)])
            if not n:
                return False
        except:
            return False 
    return True
