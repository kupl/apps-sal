def shades_of_grey(n):
    return [
        '#{0}{0}{0}'.format('{0:02x}'.format(i))
        for i in range(1, 1 + max(0, min(n, 254)))]
