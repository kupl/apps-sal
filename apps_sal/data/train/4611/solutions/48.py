def animals(heads, legs):
    for i in range(501):
        for j in range(251):
            if heads == i+j and i*2 + j*4 == legs:
                return i,j
    return "No solutions"
