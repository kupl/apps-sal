import collections

def next_item(xs, item):
    try:
        return xs[xs.index(item) + 1]
    except AttributeError:
        try:
            while next(xs) != item:
                continue
            return next(xs)
        except StopIteration:
            return None
    except (ValueError, IndexError):
        return None
