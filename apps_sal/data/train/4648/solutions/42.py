def automorphic(n):
    flag = str(n ** 2).endswith(str(n))
    return 'Automorphic' if flag else 'Not!!'
