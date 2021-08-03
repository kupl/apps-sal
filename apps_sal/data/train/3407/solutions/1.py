def palindrome_chain_length(n, count=0):
    if str(n) == str(n)[::-1]:
        return count
    else:
        return palindrome_chain_length(n + int(str(n)[::-1]), count + 1)
