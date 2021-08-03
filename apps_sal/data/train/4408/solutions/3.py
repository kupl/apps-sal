def yoga(classroom, poses):
    result = 0
    for row in classroom:
        s = sum(row)
        result += sum(s + x >= p for x in row for p in poses)
    return result
