from io import StringIO


def move(n, a, b, c, source, target, auxiliary, output):
    if n > 0:
        move(n - 1, a, b, c, source, auxiliary, target, output)
        target.append(source.pop())
        print([a, b, c], file=output)
        move(n - 1, a, b, c, auxiliary, target, source, output)


def hanoiArray(n):
    (a, b, c) = (list(range(n, 0, -1)), [], [])
    with StringIO() as output:
        print([a, b, c], file=output)
        move(n, a, b, c, a, c, b, output)
        return output.getvalue().rstrip('\n')
