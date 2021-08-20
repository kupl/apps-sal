def palindrome_chain_length(n):
    s = str(n)
    s_rev = s[::-1]
    count = 0
    while s != s[::-1]:
        temp = int(s)
        rev = int(s[::-1])
        test = temp + rev
        s = str(test)
        count += 1
    return count
