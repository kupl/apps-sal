def num_blocks(width, length, height):

    def linsum(n):
        return n * (n + 1) // 2

    def sqrsum(n):
        return n * (n + 1) * (2 * n + 1) // 6
    cube = width * length * height
    stairs = (width + length) * linsum(height - 1)
    corner = sqrsum(height - 1)
    return cube + stairs + corner
