def lcs(string1, string2):
    if not string1 or not string2:
        return ''
    if string1[0] == string2[0]:
        return string1[0] + lcs(string1[1:], string2[1:])

    return max(lcs(string1, string2[1:]), lcs(string1[1:], string2), key=len)

