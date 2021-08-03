def is_palindrome(s):
    s = s.lower()
    if len(s) == 1:
        return True
    else:
        A = s[:len(s) // 2]
        B = s[len(s) // 2:]
        if len(B) > len(A):
            B = B[1:]
        if A == B[::-1]:
            return True
    return False
