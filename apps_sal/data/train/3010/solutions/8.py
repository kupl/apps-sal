def solution(pairs):
    return ','.join(('{} = {}'.format(k, v) for (k, v) in sorted(pairs.items())))
