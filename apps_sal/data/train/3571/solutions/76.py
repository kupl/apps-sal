def is_divisible(wall_length, pixel_size):
    return wall_length % pixel_size == 0


def main():
    is_divisible(4050, 27)


main()
