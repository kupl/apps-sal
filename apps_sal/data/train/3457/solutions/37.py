def final_grade(points, project):
    if points > 90 or project > 10:
        point = 100
    elif points > 75 and project >= 5:
        point = 90
    elif points > 50 and project >= 2:
        point = 75
    else:
        point = 0
    return point
