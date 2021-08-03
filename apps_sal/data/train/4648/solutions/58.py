true = "Automorphic"
false = "Not!!"


def automorphic(n):
    return true if str(n) == str(n * n)[-len(str(n)):] else false
