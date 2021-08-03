def palindrome_chain_length(n):
    x = list(str(n))
    result = 0
    while x != x[::-1]:
        n = n + int(''.join(x[::-1]))
        x = list(str(n))

        result += 1
    return result
