def animals(heads, legs):
    chickens = -legs/2+2*heads
    cows = legs/2-heads
    return (chickens,cows) if chickens>=0 and cows>=0 and chickens.is_integer() and cows.is_integer() else 'No solutions'
