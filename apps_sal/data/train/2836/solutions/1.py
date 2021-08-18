def find_screen_height(width, ratio):
    z = ratio.split(":")

    height = (width / int(z[0])) * int(z[1])

    return f"{width}x{int(height)}"
