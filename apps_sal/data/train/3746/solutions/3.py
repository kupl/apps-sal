def is_palindrome(n):
    return str(n)[::-1] == str(n)


def next_pal(val):
    for i in range(val + 1, 10 * val):
        if is_palindrome(i):
            return i
