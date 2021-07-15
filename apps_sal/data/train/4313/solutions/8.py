def box_capacity(length, width, height):
    # Your code here.
    box_length = length * 12 // 16
    width_box = width * 12 // 16
    height_box = height * 12 // 16
    
    return box_length * width_box * height_box

