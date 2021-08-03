def avg(lst):
    return sum(lst) / len(lst)


def better_than_average(class_points, your_points):
    # Your code here
    # return True if your_points > sum(class_points) / len(class_points) else return False
    if your_points > avg(class_points):
        return True
    else:
        return False
