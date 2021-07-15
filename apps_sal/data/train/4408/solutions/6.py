yoga = lambda classroom, poses: sum(sum(len([1 for p in poses if p<=c+sum(r)]) for c in r) for r in classroom)

