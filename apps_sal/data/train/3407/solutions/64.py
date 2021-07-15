def palindrome_chain_length(x):
    
    def f(x):
        return str(int(x) + int("".join(list(reversed(x)))))
        
    def isPalindrome(s): 
        return s == s[::-1] 
    
    n = 0
    x = str(x)
    while True:
        
        if isPalindrome(x):
            return n
    
        else:
            x = f(x)
            n = n + 1
