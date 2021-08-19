def automorphic(n):
    square = n ** 2
    return 'Automorphic' if str(n)[::-1] == str(square)[::-1][:len(str(n))] else 'Not!!'
