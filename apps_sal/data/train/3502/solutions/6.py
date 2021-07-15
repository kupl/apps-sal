def solution(*args):
    return True if [x for x in args if args.count(x) > 1] else False
