def uni_total(string):
    s = string
    count = 0
    if s == '':
        return 0
    for x in range(len(s)):
        count = count + ord(s[x])
    return count
