def box_capacity(length, width, height):
    length_capacity = length * 12 // 16
    width_capacity = width * 12 // 16
    height_capacity = height * 12 // 16
    return length_capacity * width_capacity * height_capacity
