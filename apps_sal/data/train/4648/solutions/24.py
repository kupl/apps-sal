def automorphic(n):
    res = n ** 2
    if str(n) in str(res):
        return 'Automorphic'
    else:
        return 'Not!!'
