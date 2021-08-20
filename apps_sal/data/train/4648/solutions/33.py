def automorphic(n):
    if n == 1:
        return 'Automorphic'
    else:
        x = str(int(n ** 2))
        n = str(n)
        print(x[len(x) - len(n):])
        if n != x[len(x) - len(n):]:
            return 'Not!!'
        else:
            return 'Automorphic'
