def black_and_white(height, width, compressed):
    result = [list() for _ in range(height)]
    line_idx = 0
    for i, c in enumerate(compressed):
        black = (i % 2 == 0)
        while c:
            if sum(result[line_idx]) == width:
                if len(result[line_idx]) % 2 != 0:
                    result[line_idx].append(0)
                line_idx += 1
            if len(result[line_idx]) == 0 and not black:
                result[line_idx].append(0)
            m = min(c, width - sum(result[line_idx]))
            result[line_idx].append(m)
            c -= m
    if len(result[line_idx]) % 2 != 0:
        result[line_idx].append(0)
    return result
