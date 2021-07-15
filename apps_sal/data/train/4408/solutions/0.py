def yoga(classroom, poses):
    total_poses = 0
    for pose in poses:
        for row in classroom:
            for person in row:
                if person + sum(row) >= pose:
                    total_poses += 1
    return total_poses
