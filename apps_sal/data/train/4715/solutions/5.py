def build_palindrome(s):
    if list(s) == list(s)[::-1]:
        return s
    for i in range(1, len(s)):
        if s[i:] == s[i:][::-1]:
            break
    endAdd = s + s[0:i][::-1]
    for i in range(1, len(s)):
        if s[:-i] == s[:-i][::-1]:
            break
    frontAdd = s[-i:][::-1] + s
    print(endAdd)
    print(frontAdd)
    if len(list(endAdd)) <= len(list(frontAdd)):
        return endAdd
    else:
        return frontAdd
