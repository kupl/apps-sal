def is_palindrome(s):
    """Check if s is a palindrome"""
    return s == s[::-1]


def left_strip_palindrome(s):
    """Keeps stripping from left to find a palindrome. If not found return None. 
    If found return the stripped characters in stripping order"""
    for i in range(len(s) - 1):
        if is_palindrome(s[i:]):
            return s[:i]
    return None


def right_strip_palindrome(s):
    """Keeps stripping from right to find a palindrome. If not found return None. 
    If found return the stripped characters in stripping order"""
    for i in range(-1, 1 - len(s), -1):
        if is_palindrome(s[:i]):
            return s[i:]


def build_palindrome(s):
    """Build a palindrome by adding the min number of characters possible."""
    lsp = left_strip_palindrome(s)
    rsp = right_strip_palindrome(s)
    if lsp is not None:
        lsp_ans = s + lsp[::-1]
        if rsp is not None:
            rsp_ans = rsp[::-1] + s
            return min((lsp_ans, rsp_ans), key=len)
        return lsp_ans
    if rsp is not None:
        rsp_ans = rsp[::-1] + s
        return rsp_ans
    return s[1:][::-1] + s
