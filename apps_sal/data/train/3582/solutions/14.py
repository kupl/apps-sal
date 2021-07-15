def is_digit(n):
    try: 
        if int(n) < 10 > 0 and len(n) == 1:
            return True
        else:
            return False
    except:
        return False
