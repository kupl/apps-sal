def self_converge(number):
    (n, cycle) = (str(number), set())
    while n not in cycle:
        cycle.add(n)
        s = ''.join(sorted(n))
        n = '%0*d' % (len(n), int(s[::-1]) - int(s))
    return -1 if not int(n) else len(cycle)
