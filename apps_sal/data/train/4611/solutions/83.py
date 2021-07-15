def animals(heads, legs):
    cows = 0.5*legs - heads
    chickens = 2*heads - 0.5*legs
    return (chickens, cows) if chickens >= 0 and chickens.is_integer() and cows >=0 and cows.is_integer() else "No solutions"
