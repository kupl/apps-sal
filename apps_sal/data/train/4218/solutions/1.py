def game_winners(gryffindor, slytherin):
    g = gryffindor[0]
    s = slytherin[0]
    if gryffindor[1] == 'yes':
        g += 150
    else:
        s += 150
    if g > s:
        return 'Gryffindor wins!'
    elif g < s:
        return 'Slytherin wins!'
    else:
        return "It's a draw!"
