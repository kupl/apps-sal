def yoga(classroom, poses):
    return len([z for i in poses for k in classroom for z in k if sum(k) + z >= i])

