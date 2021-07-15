def palindrome_chain_length(n):
    a=0
    while 1:
        if n==int(str(n)[::-1]):return a 
        else:n+=int(str(n)[::-1])
        a+=1
        
    

