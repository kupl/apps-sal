def describeList(list):
    return {0: 'empty', 1: 'singleton'}.get(len(list), 'longer')
