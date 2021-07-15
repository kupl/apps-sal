def beasts(heads, tails):
    hydra = (heads - (2 * tails)) /3
    orthus = tails - ((heads - (2 * tails)) /3)
    if  hydra % 1 == 0 and hydra >= 0 and orthus % 1 == 0 and orthus >= 0:
        return [orthus, hydra]
    else:
        return f'No solutions'


