def string_expansion(s):

    def f():
        repeat = 1
        for c in s:
            if c.isdigit():
                repeat = int(c)
            else:
                yield (c * repeat)
    return ''.join(f())
