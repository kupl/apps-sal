def yoga(classroom, poses):
    return sum(1 for row in classroom for o in row for p in poses if o + sum(row) >= p)

