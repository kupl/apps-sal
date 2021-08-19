from datetime import datetime, timedelta


def delta(*span):
    (start, end) = [datetime.strptime(s, '%H:%M') for s in span]
    return (end + timedelta(days=1) if start > end else end) - start


def sort_time(arr):
    prev = '00:00'
    xs = list(arr)
    result = []
    while xs:
        i = min(enumerate(xs), key=lambda x: delta(prev, x[1][0]))[0]
        (a, prev) = xs.pop(i)
        result.append([a, prev])
    return result
