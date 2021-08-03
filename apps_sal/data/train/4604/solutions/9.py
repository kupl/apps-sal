def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return 'Not valid'
    check = str(num)
    for i in range(2, len(check) + 1):
        for j in range(len(check) - i + 1):
            if is_palin(check[j:j + i]):
                return True
    return False


def is_palin(s):
    return s[::-1] == s
