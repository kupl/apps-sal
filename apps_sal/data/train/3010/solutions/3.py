def solution(pairs):
    return ','.join(f'{key} = {pairs[key]}' for key in sorted(pairs.keys(), key = str))
