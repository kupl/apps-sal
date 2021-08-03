def find_screen_height(width, ratio):
    # Turns the string ratio into a list with the two numbers as elements
    z = ratio.split(":")

    # calculates the height value
    height = (width / int(z[0])) * int(z[1])

    # Displays the string
    return f"{width}x{int(height)}"
