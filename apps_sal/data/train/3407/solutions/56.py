def palindrome_chain_length(n):
    strn = str(n)
    if strn == strn[::-1]:
        return 0
    else:
        count = 0
        value = strn
        while value[::-1] != value:
            value = str(int(value[::-1]) + int(value))
            count += 1
        return count
