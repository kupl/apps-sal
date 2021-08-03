def is_palindrome(n):
    n = str(n)
    if len(n) % 2:
        return n[:len(n) // 2] == n[len(n) // 2 + 1:][::-1]
    else:
        return n[:len(n) // 2] == n[len(n) // 2:][::-1]


def palindrome_chain_length(n):
    if n < 10:
        return 0
    if is_palindrome(n):
        return 0
    else:
        i = 0
        while not is_palindrome(n):
            i += 1
            n = n + int(str(n)[::-1])
        return i
