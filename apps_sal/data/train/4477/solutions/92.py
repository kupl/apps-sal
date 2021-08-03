def reverse_number(n):
    n = str(n)
    if n[0] == '-':
        new_str = n[1:]
        new_str = new_str[::-1]
        new_str = '-' + new_str
        return int(new_str)
    else:
        new_str = n[::-1]
        return int(new_str)
