from math import*

def roll_dice (rolls, sides, threshold):
    total = sides**rolls
    f1, f2,outcomes = 1,1,0
    
    for j in range(rolls, min(threshold, rolls*sides - threshold + rolls + 1)):
        k = (j - rolls)//sides
        f1 = 1
        for i in range(0, k+1):
            f1 = factorial(rolls)//(factorial(i)*factorial(rolls-i))
            f2 = factorial(j - sides*i - 1)//(factorial(j-sides*i - rolls)*factorial(rolls-1))
            outcomes += ((-1)**i)*f1*f2

    if threshold > sides*rolls: return 0.0
    elif (threshold <= rolls*sides - threshold + rolls + 1): return 1 - (outcomes/total)
    else: return (outcomes/total)
