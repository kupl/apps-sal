from collections import Counter


def longest_palindrome(s):
    if s == "":
        return 0
    s = s.upper()
    x = Counter(s)
    len = 0
    flag = False
    for i in x:
        if i.isalnum():
            if x[i] % 2 == 0:
                len += x[i]
            else:
                flag = True
                len += (x[i] - 1)
    if flag == True:
        return len + 1
    return len
