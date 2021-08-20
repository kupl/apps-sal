def is_palindrome(s):
    for (i, (a, b)) in enumerate(zip(s, s[::-1])):
        if a != b:
            return False
        if i == len(s) // 2:
            return True


def solve(st):
    for i in range(len(st)):
        if is_palindrome(st[i:] + st[:i]):
            return True
    return False
