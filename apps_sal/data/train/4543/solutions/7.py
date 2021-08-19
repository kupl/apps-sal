def shades_of_grey(n):
    return ['#' + hex(x)[2:].zfill(2) * 3 for x in range(1, min(n + 1, 255))]
