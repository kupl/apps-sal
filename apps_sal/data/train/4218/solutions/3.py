def game_winners(gryffindor, slytherin):
    g = gryffindor[0] + (150 if gryffindor[1] == 'yes' else 0)
    s = slytherin[0] + (150 if slytherin[1] == 'yes' else 0)
    return 'It\'s a draw!' if g == s else '{} wins!'.format('Gryffindor' if g > s else 'Slytherin')
