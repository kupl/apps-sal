def boxes_packing(length, width, height):
    boxes = sorted(range(len(width)), key=lambda i: length[i] * width[i] * height[i])
    for i in range(len(boxes) - 1):
        x = boxes[i]
        y = boxes[i + 1]
        rotations_x = [[length[x], width[x], height[x]], [length[x], height[x], width[x]], [width[x], length[x], height[x]], [width[x], height[x], length[x]], [height[x], length[x], width[x]], [height[x], width[x], length[x]]]
        for (lx, wx, hx) in rotations_x:
            if lx < length[y] and wx < width[y] and (hx < height[y]):
                break
        else:
            return False
    return True
