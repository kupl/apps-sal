def christmas_tree(height):
    height = height // 3 * 3
    if height <= 0:
        return ""
    lines = []
    w = 3
    for i in range(height):
        w += 2 if i % 3 else -2
        lines.append("*" * w)
    lines.append("
    return "\r\n".join(line.center(w).rstrip() for line in lines)
