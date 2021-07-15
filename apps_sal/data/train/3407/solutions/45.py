def palindrome_chain_length(n):
    pal = False
    c = 0
    while not pal:
        if str(n) == str(n)[::-1]:
            return c
        else:
            n= int(n+int(str(n)[::-1]))
            c+=1
