def moment_of_time_in_space(moment):
    t = sum(int(d) for d in moment if d.isdigit() and d != '0')
    s = sum(c == '0' or not c.isdigit() for c in moment)

    return [t < s, t == s, t > s]
