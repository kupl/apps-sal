from itertools import groupby
def solution(args):
    grps = ([v[1] for v in g] for _,g in groupby(enumerate(args), lambda p: p[1]-p[0]))
    return ','.join('{}{}{}'.format(g[0],'-'if len(g)>2 else',',g[-1])
        if len(g)>1 else str(g[0]) for g in grps)
