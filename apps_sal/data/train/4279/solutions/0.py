from collections import defaultdict
def group_in_10s(*args):
    if not args: return []
    tens = defaultdict(list)
    for n in sorted(args): tens[n//10].append(n)
    return [tens.get(d, None) for d in range(max(tens) + 1)]
