def fight(green, blue):
    xs = [(max(g - b, 0), max(b - g, 0)) for g, b in zip(green, blue)]
    return ([x for x in ys if x] for ys in zip(*xs))


def lemming_battle(battlefield, green, blue):
    while green and blue:
        green = sorted(green, reverse=True)
        blue = sorted(blue, reverse=True)
        n = min(battlefield, len(green), len(blue))
        green[:n], blue[:n] = fight(green[:n], blue[:n])
    soldiers = green or blue
    if soldiers:
        return '{} wins: {}'.format('Green' if green else 'Blue', ' '.join(map(str, sorted(soldiers, reverse=True))))
    return 'Green and Blue died'
