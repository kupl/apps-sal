def list_depth(xs, depth=0):
    if isinstance(xs, list):
        return max((list_depth(x, depth + 1) for x in xs), default=depth + 1)
    return depth
