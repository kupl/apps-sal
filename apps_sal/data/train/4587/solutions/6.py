def range_parser(string):

    def f():
        for x in string.split(','):
            if '-' in x:
                if ':' in x:
                    (x, step) = x.split(':')
                    step = int(step)
                else:
                    step = 1
                (a, b) = map(int, x.split('-'))
                yield from range(a, b + 1, step)
            else:
                yield int(x)
    return list(f())
