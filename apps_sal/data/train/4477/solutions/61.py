def reverse_number(n):
    if n < 0:
        n = str(n)
        s = n[1:len(n)]
        new_n = n[0] + s[::-1]
        return int(new_n)
    else:
        n = str(n)
        n = n[::-1]
        return int(n)
