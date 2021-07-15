def game_winners(gryffindor, slytherin):
    g, s = map(lambda arr: arr[0] + 150 * (arr[1] == 'yes'), [gryffindor, slytherin])
    return ('Slytherin wins!', 'Gryffindor wins!', "It's a draw!")[(g > s) + 2 * (g == s)]
