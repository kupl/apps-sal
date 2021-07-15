def palindrome(num):
    if type(123)!=type(num) : return 'Not valid' 
    n = str(num)
    if any(not c.isdigit() for c in n): return 'Not valid'
    l = len(n)
    return any(n[i]==n[i+1] for i in range(l-1)) or any(n[i]==n[i+2] for i in range(l-2))
