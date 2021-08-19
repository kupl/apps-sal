def args_count(*arg, **karg):
    args = []
    for (k, v) in karg.items():
        args.append(v)
    for a in arg:
        args.append(a)
    return len(args)
