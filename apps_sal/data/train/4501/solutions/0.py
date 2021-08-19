import re


def inside_out(s):
    return re.sub('\\S+', lambda m: inside_out_word(m.group()), s)


def inside_out_word(s):
    (i, j) = (len(s) // 2, (len(s) + 1) // 2)
    return s[:i][::-1] + s[i:j] + s[j:][::-1]
