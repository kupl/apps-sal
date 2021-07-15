def animals(heads, legs):
    Chickens = (4*heads - legs)/2
    Cows = heads - Chickens
    return (Chickens, Cows) if Cows >= 0 and Chickens >= 0 and int(Chickens) == Chickens  else "No solutions"
