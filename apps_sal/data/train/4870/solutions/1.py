from statistics import mean


def redistribute_wealth(wealth):
    avg = mean(wealth)
    for i in range(len(wealth)):
        wealth[i] = avg

