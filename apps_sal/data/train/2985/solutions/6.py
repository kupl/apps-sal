def reflections(max_x, max_y):
    return bool(max_x & -max_x & (max_y & -max_y))
