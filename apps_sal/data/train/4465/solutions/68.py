def super_size(n):
    x =[i for i in str(n)]
    x = sorted(x, reverse= True)
    return int("".join(x))
