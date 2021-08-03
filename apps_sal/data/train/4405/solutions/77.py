def is_palindrome(a):
    a = str(a)
    i, n = 0, len(a) - 1
    while i < n:
        if a[i] != a[n]:
            return False
        i, n = i + 1, n - 1
    return True
