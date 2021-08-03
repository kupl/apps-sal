def solve(s):
    s1 = s[::-1]
    s2 = ''
    for i in s1:
        if i.isalpha():
            s2 += i
        elif i.isdigit():
            s2 = s2 * int(i)
    return s2[::-1]
