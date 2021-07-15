def palindrome_chain_length(n):
    x = 0
    
    while list(str(n)) != list(str(n))[::-1]:
        n += int(''.join(list(str(n))[::-1]))
        x += 1
    
    return x
