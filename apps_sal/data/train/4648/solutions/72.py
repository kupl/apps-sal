def automorphic(n):
    list = [num for num in str(n ** 2)]
    if str(n) in ''.join(list[-len(str(n)):]):
        return 'Automorphic'
    else:
        return 'Not!!'
