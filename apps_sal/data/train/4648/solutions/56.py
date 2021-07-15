def automorphic(n):
    s = n ** 2
    s = str(s)
    if s[-len(str(n)):] == str(n):
        return "Automorphic"
    else:
        return "Not!!"
