def automorphic(n):
    end = str(n**2)[-len(str(n)):]
    return 'Automorphic' if end==str(n) else 'Not!!'
