def winner(deck_steve, deck_josh):
    ls = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    st = 0
    jo = 0
    for k, v in enumerate(deck_josh):
        if ls.index(v) > ls.index(deck_steve[k]):
            jo += 1
        elif ls.index(v) < ls.index(deck_steve[k]):
            st += 1
    return "Tie" if st == jo else "{} wins {} to {}".format('Steve' if st > jo else "Josh", max(st, jo), min(st, jo))
