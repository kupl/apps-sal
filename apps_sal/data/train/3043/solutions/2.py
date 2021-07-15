def print_nums(*args):
    return "\n".join("{:0{}}".format(n, len(str(max(args)))) for n in args) if args else ""
