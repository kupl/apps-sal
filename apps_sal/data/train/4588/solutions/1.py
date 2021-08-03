def controller(events):
    state = 0
    movement = False
    direction = True
    output = ''
    for event in events:
        if event is 'P':
            movement = not movement
        if event is 'O':
            direction = not direction
        state = state + (-1, 1)[direction] * movement
        if state in (0, 5):
            direction = not state
            movement = False
        output += str(state)
    return output
