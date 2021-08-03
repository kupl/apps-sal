def is_palindrome(s):
    k = list(s.lower())
    for d, i in enumerate(k):
        if i != k[len(k) - (d + 1)]:
            return False
    return True
