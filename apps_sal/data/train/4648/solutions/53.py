def automorphic(n):
    n_sqr_str = str(n ** 2)
    return 'Automorphic' if n_sqr_str[-len(str(n)):] == str(n) else 'Not!!'
