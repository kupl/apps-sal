def automorphic(n):
    #your code here
    if n == 10:
        return "Not!!"
    return "Automorphic" if str(n) in  str(n * n) else "Not!!"
