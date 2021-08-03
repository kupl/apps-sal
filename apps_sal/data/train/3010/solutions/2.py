def solution(d): return ",".join("{} = {}".format(*p)for p in sorted(d.items()))
