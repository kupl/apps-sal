def evil(n):
    binario = bin(n)[2::]
    unos = binario.count("1")
    return "It's Odious!" if unos%2!=0 else "It's Evil!"
