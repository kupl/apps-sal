def palindrome_chain_length(n):
    if str(n) == str(n)[::-1]:
        return 0
    res, count = n, 0
    while True:
        count += 1
        res += int(str(res)[::-1])
        if str(res) == str(res)[::-1]:
            return count
    return count
