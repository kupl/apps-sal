def boxes_packing(length, width, height):
    boxes = sorted([sorted(b) for b in zip(length, width, height)])
    return all((all((x < y for (x, y) in zip(a, b))) for (a, b) in zip(boxes, boxes[1:])))
