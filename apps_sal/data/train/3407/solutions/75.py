def palindrome_chain_length(n):
    reverse = int(str(n)[::-1])
    length = 0
    
    while (n != reverse):
        n += reverse
        reverse = int(str(n)[::-1])
        length += 1
        
    return length
