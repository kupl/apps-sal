def find_screen_height(width: int, ratio: str) -> str:
    """" Get screen dimensions as a string written as WIDTHxHEIGHT based on width and ratio. """
    (_width_ratio, _height_ratio) = ratio.split(':')
    return f'{width}x{int(width / int(_width_ratio) * int(_height_ratio))}'
