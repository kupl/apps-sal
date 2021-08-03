def palindrome(num):
    if type(num) != int or num < 0:
        return "Not valid"
    s = str(num)
    count, ls = 0, len(s)
    for i in range(ls - 2):
        for d in [1, 2]:
            if s[i] == s[i + d]:
                offset = 1
                while 0 <= i - offset and i + d + offset < ls and s[i - offset] == s[i + d + offset]:
                    offset += 1
                count += offset
    return count + (ls != 1 and s[-1] == s[-2])
