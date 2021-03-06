import math


def is_palindrome(n):
    rev = 0
    num = n
    while n > 0:
        dig = math.floor(n % 10)
        rev = rev * 10 + dig
        n = math.floor(n / 10)
    return True if num == rev else False


def reverse(n):
    if n < 0:
        return None
    rev = 0
    while n > 0:
        dig = math.floor(n % 10)
        rev = rev * 10 + dig
        n = math.floor(n / 10)
    return rev


def palindrome_chain_length(n):
    step = 0
    while not is_palindrome(n):
        n += reverse(n)
        step += 1
    return step
