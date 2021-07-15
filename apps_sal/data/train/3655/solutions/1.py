def my_crib(n):
    roof = [("/" + " "*k + "\\").center(2*n+2) for k in range(0, 2*n, 2)]
    ceiling = ["/" + "_"*2*n + "\\"]
    walls = ["|" + " "*2*n + "|"]*(n-1)
    floor = ["|" + "_"*2*n + "|"]
    return "\n".join(roof + ceiling + walls + floor)
