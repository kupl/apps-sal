def animals(heads, legs):
    cows = (legs-2*heads)/2
    chicken = heads - cows
    return ((chicken, cows) if cows == int(cows) and cows>=0 and chicken >=0 else "No solutions")
