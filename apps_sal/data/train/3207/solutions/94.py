def reverseWords(str):
    s = str.split(' ')
    ans = ''
    for i in range(len(s) - 1, -1, -1):
        if i != len(s) - 1:
            ans += ' '
        ans += s[i]
    return ans
