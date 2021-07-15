def yoga(classroom, poses):
    if not classroom or not poses:
        return 0
    res = 0
    for row in classroom:
        row_sum = sum(row)
        for pose in poses:
            for person in row:
                if person + row_sum >= pose:
                    res += 1
    return res
