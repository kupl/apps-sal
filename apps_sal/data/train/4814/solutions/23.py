def is_palindrome(s):
    s = s.lower()
    start = 0
    end = -1
    palindrome = True
    for x in range(int(len(s))):
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:
            palindrome = False
    if palindrome is True:
        return True
    else:
        return False
