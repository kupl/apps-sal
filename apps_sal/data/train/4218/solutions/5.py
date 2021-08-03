def game_winners(gryffindor, slytherin):
    sbonus = 0
    bonus = 0
    if gryffindor[1] == "yes":
        bonus = 150
    else:
        bonus = 0
    if slytherin[1] == "yes":
        sbonus = 150
    else:
        sbonus = 0
    if gryffindor[0] + bonus > slytherin[0] + sbonus:
        return "Gryffindor wins!"
    elif gryffindor[0] + bonus < slytherin[0] + sbonus:
        return "Slytherin wins!"
    else:
        return "It's a draw!"
