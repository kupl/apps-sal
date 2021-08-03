def symmetric_point(p, center):
    px, py = p
    cx, cy = center
    return [cx - (px - cx), cy - (py - cy)]
