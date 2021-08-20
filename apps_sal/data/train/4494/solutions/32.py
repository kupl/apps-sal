def points(games):

    def calculate(args):
        return 0 if args[1] > args[0] else 1 if args[1] == args[0] else 3
    return sum([calculate(scores.split(':')) for scores in games])
