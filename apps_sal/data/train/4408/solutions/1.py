def yoga(classroom, poses):
    return sum((1 for r in classroom for v in r for p in poses if p <= v + sum(r)))
