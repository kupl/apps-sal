from collections import Counter as C
r=dict(zip("road settlement city development".split(),map(C,"bw bwsg ooogg osg".split())))
build_or_buy=lambda s:(lambda t:[k for k,v in r.items()if all(v[x]<=t[x]for x in v)])(C(s))
