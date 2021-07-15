def reverse_number(n):
    try:
        return int(str(n)[::-1])
    except:
        return int(str(n)[:0:-1]) * -1
