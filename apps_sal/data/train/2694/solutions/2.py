points = {"life": 0, "eating": 1, "kata": 5, "Petes kata": 10}


def paul(lst):
    score = sum(points[activity] for activity in lst)
    return "Super happy!" if score < 40 else "Happy!" if score < 70 else "Sad!" if score < 100 else "Miserable!"
