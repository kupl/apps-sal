def game_winners(gryffindor, slytherin):
    g = gryffindor[0] + 150 * (gryffindor[1] == 'yes')
    s = slytherin[0] + 150 * (slytherin[1] == 'yes')
    return 'Gryffindor wins!' if g > s else 'Slytherin wins!' if s > g else "It's a draw!"
