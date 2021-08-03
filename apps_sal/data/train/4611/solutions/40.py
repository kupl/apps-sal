def animals(heads, legs):
    chicken = heads * 2 - legs / 2
    cows = heads - chicken
    return "No solutions" if chicken < 0 or cows < 0 or chicken != int(chicken) else (chicken, cows)
