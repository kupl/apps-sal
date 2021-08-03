def solve(s):
    mayus = 0
    minus = 0
    for i in range(len(s)):
        if (ord(s[i]) >= 97 and ord(s[i]) <= 122):
            minus += 1
        elif (ord(s[i]) >= 65 and ord(s[i]) <= 90):
            mayus += 1
    if minus > mayus or mayus == minus:
        return s.lower()
    else:
        return s.upper()
