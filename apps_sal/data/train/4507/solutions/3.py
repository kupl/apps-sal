def endless_string(s, start, l):
    s = s * 500
    half = len(s) // 2
    return s[half + start:half + start + l] if l > 0 else s[half + start + l + 1:half + start + 1]
