def game(maxMike, maxJoe):
    roundsMike = int(maxMike ** 0.5)
    roundsJoe = (-1 + (1 + 4 * maxJoe) ** 0.5) // 2
    return "Non-drinkers can't play" if not maxMike or not maxJoe else 'Joe' if roundsMike <= roundsJoe else 'Mike'
