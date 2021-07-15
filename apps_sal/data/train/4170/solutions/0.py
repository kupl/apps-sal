def super_sum(D, N):
    #Number of possible combinations of D length from set [0...N]
    num = pow(N,D)
    #2x average value of a combination; 2x because dividing results in float and loss of precision
    dblAvg = D*(N-1)
    #Multiply number of possible combinations by the avergae value; now use true division to ensure result is an integer
    return num*dblAvg//2
