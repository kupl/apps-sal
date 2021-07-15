def palindrome_chain_length(n):
    s=str(n)
    for i in range(0,50):
        if s==s[::-1]:
            return i
        else:
            s=str(int(s)+int(s[::-1]))
