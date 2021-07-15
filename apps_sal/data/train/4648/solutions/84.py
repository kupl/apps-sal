def automorphic(n):
    squared = str(n**2)
    n = str(n)
    if squared[-len(n):] == n:
        return "Automorphic"
    return "Not!!"
