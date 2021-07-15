def automorphic(n):
    square = str(n*n)
    convertedN = len(str(n))
    return 'Automorphic' if square[-convertedN::]==str(n) else 'Not!!'
