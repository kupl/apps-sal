def args_to_string(args):
    r = []
    for a in args:
        if type(a) == list:
            if len(a) == 1:
                r += a[0],
            else:
                s = '-'
                if len(a[0]) > 1:
                    s += '-'
                r += s + ' '.join(a),
        else:
            r += a,
    return' '.join(r)
