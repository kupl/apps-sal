def palindrome(n):
    if type(n) == int and n > 0:
        n1,n2 = str(n),str(n)[::-1]
        return n1 == n2
    else:
        return 'Not valid'

