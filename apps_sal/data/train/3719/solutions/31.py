def starting_mark(height):
    #    return round(height * 3.937 +3.4655,2)
    return round((height / 0.0254 * 3.937 + 136.43) * 0.0254, 2)
