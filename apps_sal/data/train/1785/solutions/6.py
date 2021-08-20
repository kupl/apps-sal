def gen_id():
    i = 1
    while True:
        yield i
        i += 1


def dithering(width, height):
    """yields coordinates in the given pixmap"""
    result = []
    pix_map = []
    max_step = 1
    while max_step <= max(width - 1, height - 1):
        max_step *= 2
    for i in range(height):
        temp_list = [0] * width
        pix_map.append(temp_list)
    start = (0, 0)
    recursion(result, 1, max_step, start, pix_map)
    for i in result:
        yield i


def recursion(result, step, max_step, start, pix_map):
    if step * 2 <= max_step:
        recursion(result, step * 2, max_step, (start[0], start[1]), pix_map)
        recursion(result, step * 2, max_step, (start[0] + step, start[1] + step), pix_map)
        recursion(result, step * 2, max_step, (start[0], start[1] + step), pix_map)
        recursion(result, step * 2, max_step, (start[0] + step, start[1]), pix_map)
    if len(pix_map) > start[0] and len(pix_map[start[0]]) > start[1] and (pix_map[start[0]][start[1]] == 0):
        pix_map[start[0]][start[1]] = num_gen.__next__()
        result.append((start[1], start[0]))
    if len(pix_map) > start[0] + step and len(pix_map[start[0]]) > start[1] + step and (pix_map[start[0] + step][start[1] + step] == 0):
        pix_map[start[0] + step][start[1] + step] = num_gen.__next__()
        result.append((start[1] + step, start[0] + step))
    if len(pix_map) > start[0] and len(pix_map[start[0]]) > start[1] + step and (pix_map[start[0]][start[1] + step] == 0):
        pix_map[start[0]][start[1] + step] = num_gen.__next__()
        result.append((start[1] + step, start[0]))
    if len(pix_map) > start[0] + step and len(pix_map[start[0]]) > start[1] and (pix_map[start[0] + step][start[1]] == 0):
        pix_map[start[0] + step][start[1]] = num_gen.__next__()
        result.append((start[1], start[0] + step))


num_gen = gen_id()
