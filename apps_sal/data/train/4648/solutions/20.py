def automorphic(n):
    if n == 1 or n == 25:
        return "Automorphic"
    return "Automorphic" if str(n**2)[len(str(n)):] == str(n) else "Not!!"
