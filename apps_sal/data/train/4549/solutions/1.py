def lemming_battle(battlefield, green, blue):
    battlefield = min(battlefield, len(green), len(blue))
    while sum(green) and sum(blue):
        green, blue = sorted(green, reverse=True), sorted(blue, reverse=True)
        for i in range(battlefield):
            green[i], blue[i] = max(0, green[i] - blue[i]), max(0, blue[i] - green[i])
    if not sum(green) + sum(blue):
        return "Green and Blue died"
    winner = "green" if sum(green) else "blue"
    survivors = " ".join(str(lemming) for lemming in sorted(locals()[winner], reverse=True) if lemming)
    return f"{winner.title()} wins: {survivors}"
