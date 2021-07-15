def capitalize(s):
    s = s.lower()
    even_str = ''
    for i in range(len(s)):
        if i % 2 == 0:
            even_str += s[i].upper()
        else:
            even_str += s[i]
    return [even_str, even_str.swapcase()]
