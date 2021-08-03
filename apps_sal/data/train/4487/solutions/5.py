def order_type(arr):
    len_stats = [len(str(x)) if type(x) == int else len(x) for x in arr]
    sorted_stats = sorted(len_stats)

    if not arr or sorted_stats[0] == sorted_stats[-1]:
        return "Constant"

    if len_stats == sorted_stats:
        return "Increasing"

    return "Decreasing" if len_stats == sorted_stats[::-1] else "Unsorted"
