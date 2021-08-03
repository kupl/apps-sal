def automorphic(n):
    return {True: "Automorphic", False: "Not!!"}[str(n) == str(n**2)[-len(str(n)):]]
