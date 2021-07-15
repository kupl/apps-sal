def array_madness(a,b):
    squaresA = 0
    cubesB = 0
    for i in range(len(a)):
        squaresA += pow(a[i], 2)
    for j in range(len(b)):
        cubesB += pow(b[j], 3)  
    return squaresA > cubesB
