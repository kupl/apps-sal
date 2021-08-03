def automorphic(n):
    print(n)
    # your code here
    sqr = n**2
    l = len(str(n))
    if str(sqr)[-l:] == str(n):
        return "Automorphic"
    else:
        return 'Not!!'
