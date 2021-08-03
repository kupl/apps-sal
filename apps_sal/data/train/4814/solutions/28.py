def is_palindrome(s):
    n = len(s)
    l = 0
    r = n - 1
    res = True
    s = s.lower()
    if(n == 0 or n == 1):
        return res
    else:
        while(l < r):
            if(s[l] != s[r]):
                res = False
                break
            l += 1
            r -= 1
        return res
