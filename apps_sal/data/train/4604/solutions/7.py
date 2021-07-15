def palindrome(n):
    return 'Not valid' if type(n) != int or n < 0 else any(s == s[::-1] for s in subs(str(n)))
        
def subs(s):
    return [s[i:i+j] for j in range(2, len(s)+1) for i in range(len(s)-j+1)]
