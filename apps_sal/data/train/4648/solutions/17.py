def automorphic(n):
    return "Automorphic" if n == int(str(n * n)[-len(str(n)) :]) else "Not!!"
