def game_winners(*scores):
    (gry, sly) = (ch + 150 * (gs == 'yes') for (ch, gs) in scores)
    return "It's a draw!" if gry == sly else f"{('Gryffindor' if gry > sly else 'Slytherin')} wins!"
