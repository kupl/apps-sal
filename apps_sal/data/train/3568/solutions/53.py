def bumps(road):
    flat = []
    bump = []
    for letter in road:
        if letter is "_":
            flat.append(letter)
        else:
            bump.append(letter)
    if len(bump) <= 15:
        return "Woohoo!"
    else:
        return "Car Dead"
