def mutually_exclusive(dice, call1, call2):
    prob_of_each_roll = []
    for roll in dice:
        prob_of_each_roll.append(roll[1])
        if roll[0] == call1:
            p1 = roll[1]
        if roll[0] == call2:
            p2 = roll[1]
    if sum(prob_of_each_roll) != 1:
        return
    else:
        total_prob = round((p1 + p2), 2)
        return ("{:.2f}".format(total_prob))
