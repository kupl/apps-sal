from collections import Counter


def majority(arr):
    try:
        c = Counter(arr)
        val = list(c.values())
        assert val.count(max(val)) == 1
        return sorted([(v, k) for k, v in list(c.items())], reverse=True)[0][1]
    except:
        return None
