def winner(deck_steve, deck_josh):
    bigOrSmall = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    m = "{} wins {} to {}"
    winSteve = 0
    winJosh = 0
    for i in range(len(deck_steve)):
        if bigOrSmall.index(deck_steve[i]) < bigOrSmall.index(deck_josh[i]):
            winJosh += 1
        elif bigOrSmall.index(deck_steve[i]) > bigOrSmall.index(deck_josh[i]):
            winSteve += 1
    if winSteve > winJosh:
        return m.format("Steve", winSteve, winJosh)
    elif winSteve < winJosh:
        return m.format("Josh", winJosh, winSteve)
    else:
        return "Tie"
