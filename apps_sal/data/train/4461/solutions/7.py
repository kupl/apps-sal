def boxes_packing(length, width, height):
    boxes = sorted(map(sorted, zip(length, width, height)))
    return all(all(d1 < d2 for d1, d2 in zip(smaller, larger)) for smaller, larger in zip(boxes, boxes[1:]))
