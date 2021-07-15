def fight(fields, green, blue):
    green, blue = sorted(green, reverse=True), sorted(blue, reverse=True)
    for i in range(min(len(green), len(blue), fields)):
        soldier_g, soldier_b = green[i], blue[i]
        if soldier_g > soldier_b:
            green[i], blue[i] = soldier_g - soldier_b, 0
        elif soldier_g < soldier_b:
            green[i], blue[i] = 0, soldier_b - soldier_g
        else:
            green[i], blue[i] = 0, 0
    green, blue = [s for s in green if s > 0], [s for s in blue if s > 0]
    return green, blue
                   


def lemming_battle(battlefields, green, blue):
    while green != [] and blue != []:
        green, blue = fight(battlefields, green, blue)
    green, blue = sorted(green, reverse=True), sorted(blue, reverse=True)
    if green or blue: 
            return (("Green" if green else "Blue") + " wins: " +
                " ".join(str(s) for s in green or blue))
    return "Green and Blue died"
