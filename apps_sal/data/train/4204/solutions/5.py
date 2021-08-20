def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    if num < 17:
        return 11
    inf = next((n for n in range(num, 0, -1) if is_palindrome(n)))
    sup = next((n for n in range(num, 2 * num) if is_palindrome(n)))
    mean = (inf + sup) / 2
    return sup if num >= mean else inf
