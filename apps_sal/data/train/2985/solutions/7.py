def reflections(max_x, max_y):
    slope = (1, 1)
    current = (1, 1)
    while current not in [(max_x, 0), (0, max_y), (max_x, max_y)]:
        if current[0] == max_x:
            slope = (-1, 1) if slope == (1, 1) else (-1, -1)
        elif current[1] == max_y:
            slope = (1, -1) if slope == (1, 1) else (-1, -1)
        elif current[0] == 0:
            slope = (1, 1) if slope == (-1, 1) else (1, -1)
        elif current[1] == 0:
            slope = (1, 1) if slope == (1, -1) else (-1, 1)
        current = (current[0]+slope[0], current[1]+slope[1])
    if current in [(0, 0), (max_x, max_y)]:
        return True
    else:
        return False
