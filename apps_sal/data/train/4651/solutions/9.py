def christmas_tree(h):
    if h < 3:
        return ''
    (h, r) = (h // 3, [])
    m = h * 2 + 3
    r = ['*' * (2 * (i + j) + 1) for i in range(h) for j in range(3)] + ['#' * 3]
    return '\r\n'.join(map(lambda x: x.center(m).rstrip(), r))
