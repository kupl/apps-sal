def game_winners(gryffindor, slytherin):
    (g, s) = (team[0] + 150 * (team[1] == 'yes') for team in [gryffindor, slytherin])
    return 'Gryffindor wins!' if g > s else 'Slytherin wins!' if s > g else "It's a draw!"
