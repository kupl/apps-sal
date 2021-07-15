def lowercase_count(strng):
    c = 0
    for i in range(len(strng)):
        if strng[i] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']:
            c = c + 1
    return c

