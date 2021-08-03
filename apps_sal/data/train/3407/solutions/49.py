def is_palindrome(v):
    return str(v) == str(v)[::-1]


def palindrome_chain_length(n):
    cnt = 0

    if is_palindrome(n):
        return cnt

    while(True):
        cnt += 1
        n = n + int(str(n)[::-1])
        if is_palindrome(n):
            return cnt
