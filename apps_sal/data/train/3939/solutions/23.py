def rps(*args):
    return 'Draw!' if len(set(args)) == 1 else 'Player {} won!'.format(1 + args.index('rock' if set(args) == {'rock', 'scissors'} else max(args, key=len)))
