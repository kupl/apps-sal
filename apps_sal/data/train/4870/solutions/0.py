def redistribute_wealth(wealth):
    wealth[:] = [sum(wealth) / len(wealth)] * len(wealth)
