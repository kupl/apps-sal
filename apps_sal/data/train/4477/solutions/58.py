def reverse_number(n):
    if n < 0:
        return - int(str(n)[1:][::-1])
    try:
        return int(str(n).rstrip("0")[::-1])
    except:
        return 0
