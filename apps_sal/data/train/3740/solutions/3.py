
def mins(time): return (lambda res: int(res[0]) * 60 + int(res[1]))(time.split(":"))


def dt(a, b): return (lambda diff: 1440 + diff if diff < 0 else diff)(mins(a) - mins(b))


sort_time = lambda arr, last="00:00": [arr[0]] if len(arr) == 1 else (lambda arr: [arr[0]] + sort_time(arr[1:], arr[0][1]))(sorted(arr, key=lambda a: dt(a[0], last)))
