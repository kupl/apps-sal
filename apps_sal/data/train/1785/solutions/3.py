from math import ceil, log2


def dithering(width, height):
    """yields coordinates in the given pixmap"""
    pow2dim = max(ceil(log2(x)) for x in [width, height])
    pos = [0] * (pow2dim)
    for _ in range((2**pow2dim)**2):
        x, y = 0, 0
        for idx in range(pow2dim):
            if pos[idx] in [1, 2]:
                x += 2**(pow2dim - idx - 1)
            if pos[idx] in [1, 3]:
                y += 2**(pow2dim - idx - 1)
        if x < width and y < height:
            yield x, y
        for idx in range(pow2dim):
            pos[idx] = (pos[idx] + 1) % 4
            if pos[idx] > 0:
                break
