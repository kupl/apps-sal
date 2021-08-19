def controller(events):
    result = []
    (pos, moving, direction) = (0, False, 1)
    for e in events:
        if e == 'P':
            moving = not moving
        elif e == 'O':
            direction *= -1
        if moving:
            pos += direction
            if not 0 < pos < 5:
                direction *= -1
                moving = False
        result.append(pos)
    return ''.join(map(str, result))
