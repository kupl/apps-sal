def bumps(road):
    # your code here
    bump = 0
    for s in road:
        if s == 'n':
            bump += 1
    return "Woohoo!" if bump <= 15 else "Car Dead"
