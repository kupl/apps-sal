def box_capacity(length, width, height):
    length_i = 12 * length
    width_i = 12 * width
    height_i = 12 * height
    crate = 16
    L = length_i // crate
    W = width_i // crate
    H = height_i // crate
    return L * W * H
