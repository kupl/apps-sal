def palindrome_chain_length(n):
    def is_palindrome(x): return str(x) == str(x)[::-1]
    res = 0
    while not is_palindrome(n):
        n += int(str(n)[::-1])
        res += 1
    return res
