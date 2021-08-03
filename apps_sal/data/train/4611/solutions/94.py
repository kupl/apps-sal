def animals(heads, legs):
    cows = (legs - (heads * 2)) / 2
    chicken = heads - cows
    if cows < 0 or chicken < 0 or chicken != int(chicken):
        return "No solutions"
    return (chicken, cows)
