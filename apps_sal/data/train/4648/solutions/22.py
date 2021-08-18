def automorphic(n):
    print(n)
    sqr = n**2
    l = len(str(n))
    if str(sqr)[-l:] == str(n):
        return "Automorphic"
    else:
        return 'Not!!'
