def directions(goal):
    y = goal.count("N") - goal.count("S")
    x = goal.count("E") - goal.count("W")
    
    return ["N"] * y + ["S"] * (-y) + ["E"] * x + ["W"] * (-x)
