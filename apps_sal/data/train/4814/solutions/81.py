def is_palindrome(s):
    ns = s.lower()
    if len(ns) <= 1:
        return True
    if ns[0] != ns[-1]:
        return False
    return is_palindrome(ns[1:-1])
