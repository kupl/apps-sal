def palindrome_chain_length(n):
    n = str(n)
    if int(n) == int(str(n)[::-1]):
        return 0
    else:
        s = int(n) + int(n[::-1])
        count = 1
        while s != int(str(s)[::-1]):
            s = s + int(str(s)[::-1])
            count += 1

        return count
