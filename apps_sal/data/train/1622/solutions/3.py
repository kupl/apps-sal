def bowling_score(frames):
    pins = []
    # Identify each roll's score, bonus balls and frame
    for f, frame in enumerate(frames.split()):
        for c in frame:
            if c == "X":
                pins.append([10, 2, f])
            elif c == "/":
                p = 10 - pins[-1][0]
                pins.append([p, 1, f])
            else:
                pins.append([int(c), 0, f])
    # Apply all the bonuses
    for i in range(len(pins)):
        score, offset, frame = pins[i]
        if offset > 0 and frame < 9:
            pins[i][0] += sum(pin[0] for pin in pins[i + 1: i + 1 + offset])
    # Sum it all up
    return sum(pin[0] for pin in pins)
