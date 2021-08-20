def solution(pairs):
    return ','.join(('{} = {}'.format(key, value) for (key, value) in sorted(pairs.items())))
