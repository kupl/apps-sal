def game_winners(gryffindor, slytherin):
    (a, snitch) = gryffindor
    (b, litch) = slytherin
    if snitch == 'yes':
        if a + 150 > b:
            return 'Gryffindor wins!'
        elif a + 150 == b:
            return "It's a draw!"
        else:
            return 'Slytherin wins!'
    elif b + 150 > a:
        return 'Slytherin wins!'
    elif b + 150 == a:
        return "It's a draw!"
    else:
        return 'Gryffindor wins!'
