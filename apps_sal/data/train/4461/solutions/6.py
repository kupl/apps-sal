def boxes_packing(*args):
    boxes = sorted(map(sorted, zip(*args)))
    return all(dimension_1 < dimension_2 
                for box_1, box_2 in zip(boxes, boxes[1:]) 
                for dimension_1, dimension_2 in zip(box_1, box_2))
