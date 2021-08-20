def box_capacity(length, width, height):
    box_size = 16 / 12
    return length // box_size * (width // box_size) * (height // box_size)
