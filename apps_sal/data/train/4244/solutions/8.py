def palindrome(n):
    if not isinstance(n, int) or n < 0:
        return 'Not valid'
    if n < 9:
        return False
    n = str(n)
    return sum(n.count(c) % 2 for c in set(n)) <= 1
