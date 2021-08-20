def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    (c, s) = (0, '?' + str(num) + '!')
    for i in range(len(s) - 2):
        if s[i] == s[i + 1]:
            if s[i - 1] == s[i + 2]:
                c += 2
            else:
                c += 1
        if s[i] == s[i + 2]:
            c += 1
    return c
