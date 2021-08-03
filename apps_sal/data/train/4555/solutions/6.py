def string_color(name):
    if len(name) < 2:
        return None
    ascii = [ord(el) for el in name]
    s1 = hex(sum(ascii) % 256)[2:].upper()
    s2 = 1
    for el in ascii:
        s2 *= el
    s2 = hex(s2 % 256)[2:].upper()
    s3 = hex(abs(ascii[0] - sum(ascii[1:])) % 256)[2:].upper()
    lst = [s1, s2, s3]
    lst = ['0' + el if len(el) < 2 else el for el in lst]
    return ''.join(lst)
