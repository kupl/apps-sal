from functools import reduce


def do_math(s):
    return round(reduce(lambda a, b: [b[0], eval(''.join([str(a[1]), ['+', '-', '*', '/'][a[0] % 4], str(b[1])]))], enumerate([e[0] for e in sorted([[int(''.join([l for l in e if l.isdigit()])), ''.join([l for l in e if not l.isdigit()])] for e in s.split()], key=lambda a: a[1])]))[1])
