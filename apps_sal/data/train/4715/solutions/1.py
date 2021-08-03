def build_palindrome(s):
    a = s[1:][::-1] + s
    temp = s
    for i in range(len(s) + 1):
        temp = s[::-1][:i] + s
        if temp == temp[::-1] and len(temp) < len(a):
            a = temp

    b = s + s[::-1]
    temp = s
    for i in range(len(s) + 1):
        temp = s + s[::-1][i:]
        if temp == temp[::-1] and len(temp) < len(b):
            b = temp
    if len(a) > len(b):
        return b
    else:
        return a
