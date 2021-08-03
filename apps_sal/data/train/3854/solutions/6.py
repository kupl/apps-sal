from datetime import date


def less(d1, d2):
    if d1 == None or d2 == None:
        return 0
    return 1 if d1 <= d2 else 0


def check_dates(records):
    print(records)
    correct = recoverable = uncertain = 0
    for interval in records:
        start = interval[0].split('-')
        end = interval[1].split('-')
        try:
            a, b, c = map(int, (start[0], start[1], start[2]))
            start1 = date(a, b, c)
        except:
            start1 = None
        try:
            a, b, c = map(int, (start[0], start[2], start[1]))
            start2 = date(a, b, c)
        except:
            start2 = None
        try:
            a, b, c = map(int, (end[0], end[1], end[2]))
            end1 = date(a, b, c)
        except:
            end1 = None
        try:
            a, b, c = map(int, (end[0], end[2], end[1]))
            end2 = date(a, b, c)
        except:
            end2 = None

        combinations = less(start1, end1) + less(start1, end2) + less(start2, end1) + less(start2, end2)
        if start1 == start2:
            combinations -= 1
        if end1 == end2:
            combinations -= 1
        if start1 == start2 and end1 == end2:
            combinations -= 1

        if less(start1, end1) == 1 and combinations == 1:
            correct += 1
        elif combinations == 1:
            recoverable += 1
        else:
            uncertain += 1

    return [correct, recoverable, uncertain]
