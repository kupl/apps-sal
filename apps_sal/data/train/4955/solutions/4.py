from functools import reduce
ride = lambda g, c: "GO" if mod47(group) == mod47(comet) else "STAY"
mod47 = lambda s: reduce(lambda p, c: p * '-ABCDEFGHIJKLMNOPQRSTUVWXYZ'.index(c), s, 1) % 47

