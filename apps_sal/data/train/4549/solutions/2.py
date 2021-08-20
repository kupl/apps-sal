def lemming_battle(battlefield, green, blue):
    while True:
        (green, blue) = (sorted(green, reverse=True), sorted(blue, reverse=True))
        if not (green or blue):
            return 'Green and Blue died'
        if not green:
            return 'Blue wins: ' + ' '.join(map(str, blue))
        if not blue:
            return 'Green wins: ' + ' '.join(map(str, green))
        left = min(len(green), len(blue), battlefield)
        fight = list(map(int.__sub__, green[:left], blue[:left]))
        green = green[left:] + [x for x in fight if x > 0]
        blue = blue[left:] + [-x for x in fight if x < 0]
