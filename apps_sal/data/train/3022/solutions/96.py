import heapq


def two_highest(lst):
    if not isinstance(lst, list):
        return False
    else:
        result = []
        for it in sorted(lst, reverse=True):
            if len(result) == 0:
                result.append(it)
            elif result[0] != it:
                result.append(it)
                return result
        return result
