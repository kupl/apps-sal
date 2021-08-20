def solution(pairs):
    return ','.join(sorted(('{} = {}'.format(k, pairs[k]) for k in pairs)))
