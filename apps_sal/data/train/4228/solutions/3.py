from itertools import combinations_with_replacement as combs


def palindrome(num):
    def is_palindrome(chunk): return chunk == chunk[::-1] and len(chunk) > 1
    s, l = str(num), len(str(num))
    return len([s[i:j] for i, j in combs(range(l + 1), 2) if is_palindrome(s[i:j])]) if isinstance(num, int) and num > 0 else 'Not valid'
