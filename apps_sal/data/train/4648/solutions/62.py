def automorphic(n):
    cpy = str(n)
    n_square = n**2
    n_square = str(n_square)
    if n_square.endswith(cpy):
        return"Automorphic"
    else:
        return "Not!!"
    # your code here
