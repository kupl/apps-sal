def solution(pairs):
    return ','.join(('{} = {}'.format(k, pairs[k]) for k in sorted(pairs)))
