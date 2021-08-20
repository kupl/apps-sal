def sea_sick(sea):
    changes = sum((1 for (a, b) in zip(sea, sea[1:]) if a != b))
    return 'No Problem' if changes * 5 <= len(sea) else 'Throw Up'
