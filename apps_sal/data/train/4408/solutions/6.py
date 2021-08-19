def yoga(classroom, poses):
    return sum((sum((len([1 for p in poses if p <= c + sum(r)]) for c in r)) for r in classroom))
