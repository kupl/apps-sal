def redistribute_wealth(wealth):
    mean = sum(wealth) / len(wealth)
    wealth[:] = [mean] * len(wealth)
