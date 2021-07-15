def is_divisible(wall_length: int, pixel_size: int) -> bool:
    """
    Get a status determinig whether a wall of a certain length can 
    exactly fit an integer number of pixels of a certain length
    """
    return int(wall_length / pixel_size) == float(wall_length / pixel_size)
