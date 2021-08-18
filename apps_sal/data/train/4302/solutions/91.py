def avg(lst):
    return sum(lst) / len(lst)


def better_than_average(class_points, your_points):
    if your_points > avg(class_points):
        return True
    else:
        return False
