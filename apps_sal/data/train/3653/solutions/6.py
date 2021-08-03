def tops(s):
    tops, start = [s[2:4]], 2
    while start < len(s):
        l = len(tops[-1])
        start += (l - 1) * 2 + l * 2 + 1
        tops.append(s[start:start + l + 1])
    return "".join(tops[::-1])
