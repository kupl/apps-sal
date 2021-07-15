def redistribute_wealth(wealth):
    mean = sum(wealth) / len(wealth)
    for i, x in enumerate(wealth):
        wealth[i] = mean
