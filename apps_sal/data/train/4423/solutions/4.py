def ball_probability(balls):
    bag, draws, replaced = balls
    return round(bag.count(draws[0]) / len(bag)
                 * (bag.count(draws[1]) - (not replaced) * (draws[0] == draws[1]))
                 / (len(bag) - (not replaced)), 3)
