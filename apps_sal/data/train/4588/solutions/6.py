def controller(events: str):
    positions = []
    p = 0
    movement = False
    up = True
    for e in events:
        if e == 'P':
            movement = not movement
        if e == 'O' and movement:
            up = not up
        if movement:
            if up:
                p += 1
                if p == 5:
                    up = False
                    movement = False
            else:
                p -= 1
                if p == 0:
                    up = True
                    movement = False
        positions += [p]
    return ''.join((str(p) for p in positions))
