SIERPINSKI = {
    1: [' * ', '* *']
}


def join_lesser(fig):
    width = len(fig[-1]) + 1
    result = []
    for line in fig:
        padding = ' ' * (width // 2)
        result.append(padding + line + padding)
    for line in fig:
        result.append(line + ' ' * (width - len(line)) + line)
    return result


def get_sierpinski(n):
    if n in SIERPINSKI:
        return SIERPINSKI[n]

    lesser = get_sierpinski(n - 1)
    SIERPINSKI[n] = join_lesser(lesser)
    return SIERPINSKI[n]


def sierpinski(n):
    return '\n'.join(get_sierpinski(n))

