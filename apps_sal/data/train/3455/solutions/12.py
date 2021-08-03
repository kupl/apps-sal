def disarium_number(n):
    return ("Not !!", "Disarium !!")[sum(int(j)**i for i, j in list(enumerate(str(n), 1))) == n]
