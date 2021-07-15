def Guess_it(n,m):

    """
    n = number of balls in bag ranging from 1-50
    m = total weight of all balls in bag
    balls can be:
      green = 5 kg
      red   = 4 kg
      blue  = 3 kg
     
    return a list of all possible combinations of balls based on weight and number
  
    """
    gMass, rMass, bMass = 5, 4, 3
    gQ, rQ, bQ = 0,0,0
    massTotal = gMass*gQ + rMass*rQ + bMass*bQ
    total = gQ + rQ + bQ
    
    solutionSet = []
    while gQ <= n:
        rQ = 0
        bQ = 0
        massTotal = gMass*gQ + rMass*rQ + bMass*bQ
        total = gQ + rQ + bQ
        solution = [gQ, rQ, bQ]
        if (total, massTotal) == (n, m):
            solutionSet.append(solution)
        else:
            while gQ+rQ <= n:
                bQ = 0
                massTotal = gMass*gQ + rMass*rQ + bMass*bQ
                total = gQ + rQ + bQ
                solution = [gQ, rQ, bQ]
                if (total, massTotal) == (n, m):
                    solutionSet.append(solution)
                else:
                    while gQ + rQ + bQ <= n:
                        massTotal = gMass*gQ + rMass*rQ + bMass*bQ
                        total = gQ + rQ + bQ
                        solution = [gQ, rQ, bQ]
                        if (total, massTotal) == (n, m):
                            solutionSet.append(solution)
                        bQ += 1
                rQ += 1
        gQ += 1
    return solutionSet
