form = '#' + '{0:0>2}' * 3
def shades_of_grey(n): return [form.format(hex(i)[2:])for i in range(1, min(n + 1, 255))]
