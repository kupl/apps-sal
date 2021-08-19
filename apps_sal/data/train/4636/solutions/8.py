def dist(a, b, w=8, h=6):
    ay, ax = divmod(a, w)
    by, bx = divmod(b, w)
    dx = min((ax - bx) % w, (bx - ax) % w)
    dy = min((ay - by) % h, (by - ay) % h)
    return dx + dy


def tv_remote(words):
    num_buttons = 0

    presses = []
    mode = 0
    keypads = [
        'abcde123fghij456klmno789pqrst.@0uvwxyz_/⇧ ––––––',
        'abcde123fghij456klmno789pqrst.@0uvwxyz_/⇧ ––––––'.upper(),
        '^~?!\'"()-:;+&%*=<>€£$¥¤\\[]{},.@§#¿¡–––_/⇧ ––––––'
    ]
    for c in words:
        while True:
            if c in keypads[mode]:
                presses.append(keypads[mode].index(c))
                num_buttons += 1  # OK
                break
            mode = (mode + 1) % len(keypads)
            presses.append(keypads[mode].index('⇧'))
            num_buttons += 1  # OK shift

    cursor = 0
    for press in presses:
        print(f'{num_buttons} button moves from {cursor} to {press}')
        num_buttons += dist(cursor, press)
        cursor = press

    return num_buttons
