def palindrome_chain_length(n):
    n = str(n)
    nreverserd = n[::-1]
    count = 0
    if n == nreverserd:
        return 0
    else:
        while True:
            count += 1
            sum = int(n) + int(nreverserd)
            n = str(sum)
            nreverserd = n[::-1]
            if n == nreverserd:
                break
    return count
