def find_screen_height(width, ratio):
    a, b = map(int, ratio.split(":"))
    return f"{width}x{int(width / a * b)}"
