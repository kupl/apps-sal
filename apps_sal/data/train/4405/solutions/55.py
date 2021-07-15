def is_palindrome(string):
    s = str(string)
    return all( b==e for b, e in zip(s[:len(s)//2], s[len(s)//2:][::-1]))
