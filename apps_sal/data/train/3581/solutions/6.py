def sea_sick(sea):
    return 'Throw Up' if sum(x != y for x, y in zip(sea, sea[1:])) / len(sea) > 0.2 else 'No Problem'
