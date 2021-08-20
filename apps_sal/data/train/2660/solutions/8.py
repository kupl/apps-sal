def args_to_string(args):
    res = []
    for chunk in args:
        if type(chunk) == str:
            res.append(chunk)
        elif len(chunk) == 1:
            res.append(chunk[0])
        else:
            res.append(f"{'-' * (1 + (len(chunk[0]) > 1))}{' '.join((s for s in chunk))}")
    return ' '.join(res)
