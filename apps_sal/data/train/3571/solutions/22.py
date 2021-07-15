def is_divisible(wall_length, pixel_size):
    
    data = wall_length/pixel_size
    
    if data == int(data):
        return True
    else:
        return False
