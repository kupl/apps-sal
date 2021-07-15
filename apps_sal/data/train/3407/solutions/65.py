def palindrome_chain_length(n):
    count = 0
    while True:
        rev = int(str(n)[::-1])
        if n == rev:
            return count
        else:
            n+=rev
            count+=1
