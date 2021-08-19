def controller(events):
    (out, state, dir, moving) = ([], 0, 1, False)
    for c in events:
        if c == 'O':
            dir *= -1
        elif c == 'P':
            moving = not moving
        if moving:
            state += dir
        if state in [0, 5]:
            (moving, dir) = (False, 1 if state == 0 else -1)
        out.append(str(state))
    return ''.join(out)
