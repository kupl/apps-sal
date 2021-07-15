def find_digit(n, i):
    if i < 1: return -1
    try: return int(str(abs(n)).zfill(i)[-i])
    except: return -1
