def draw_spider(a, b, c, d):
    l = "_ ^ /\ /╲ ╱╲ ╱╲ ╱\ /\ ^".split()
    return "{}{}{}{}{}{}{}".format(l[a], "(" * b, d * 2**(b-1), c, d * 2**(b-1), ")" * b, l[-a])
