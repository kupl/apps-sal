def yoga(classroom, poses):
    new_classroom = []
    for row in classroom:
        row_sum = sum(row)
        new_row = []
        for person in row:
            new_row.append(person + row_sum)
        new_classroom.append(new_row)
    people = [person for row in new_classroom for person in row]

    result = 0
    for pose in poses:
        for person in people:
            if person >= pose:
                result += 1
    return result
