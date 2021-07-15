def solution(pairs):
    return ','.join(['{} = {}'.format(*a) for a in sorted(pairs.items())])
