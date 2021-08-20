def game_winners(gryffindor, slytherin):
    g = gryffindor[0]
    s = slytherin[0]
    if 'yes' in gryffindor[1]:
        g += 150
    elif 'yes' in slytherin[1]:
        s += 150
    if g > s:
        return 'Gryffindor wins!'
    elif g < s:
        return 'Slytherin wins!'
    else:
        return "It's a draw!"
