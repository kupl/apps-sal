def automorphic(n):
    n2 = n * n
    if str(n2).find(str(n)) == -1:
        return 'Not!!'
    elif str(n) in str(n2):
        return 'Automorphic'
    else:
        return 'Not!!'
