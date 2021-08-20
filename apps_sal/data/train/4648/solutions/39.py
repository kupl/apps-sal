def automorphic(n):
    square_num = str(n ** 2)
    num_size = len(str(n))
    if square_num[-num_size:] == str(n):
        return 'Automorphic'
    else:
        return 'Not!!'
