def get_surface_area(width, height, depth):
    return (
        (2 * depth * width)
        + (2 * depth * height)
        + (2 * height * width)
    )


def get_volume(width, height, depth):
    return width * height * depth


def get_size(width, height, depth):
    return [
        get_surface_area(width, height, depth),
        get_volume(width, height, depth)
    ]
