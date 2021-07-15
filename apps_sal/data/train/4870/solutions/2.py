from numpy import mean

def redistribute_wealth(wealth):
    wealth[:] = [mean(wealth)]*len(wealth)
