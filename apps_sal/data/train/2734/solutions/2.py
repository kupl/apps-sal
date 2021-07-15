def distance(xxx_todo_changeme, xxx_todo_changeme1):
    (x, y) = xxx_todo_changeme
    (x2, y2) = xxx_todo_changeme1
    return ((x2 - x) ** 2 + (y2 - y) ** 2) ** 0.5


def peaceful_yard(yard, min_distance):
    cats = []
    for r, row in enumerate(yard):
        for c, col in enumerate(row):
            if col != '-':
                current = (r, c)
                if any(distance(current, cat) < min_distance for cat in cats):
                    return False
                cats.append(current)
    return True

