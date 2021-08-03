def palindrome_chain_length(n):
    count = 0

    while str(n) != str(n)[::-1]:
        revn = int(str(n)[::-1])
        n = revn + n
        count += 1

    return count
