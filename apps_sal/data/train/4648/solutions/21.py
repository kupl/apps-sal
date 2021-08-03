def automorphic(n):
    return "Automorphic" if str(n) == str(n**2)[-1 * len(str(n)):] else "Not!!"
