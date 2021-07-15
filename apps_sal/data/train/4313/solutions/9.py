def box_capacity(length, width, height):
    # Your code here.
    box_size = 16/12 # in feet
    return (length//box_size) * (width // box_size) * (height//box_size)
