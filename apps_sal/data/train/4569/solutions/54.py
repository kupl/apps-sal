def next_item(xs, item):
    c = 0
    s = 0
    try:
        return xs[xs.index(item) + 1]
    except (ValueError, IndexError):
        return None
    except AttributeError:
        while True:
            try:
                t = next(xs)
                print(t)
                if c == 1:
                    s = t
                    break
                if t == item:
                    c = 1
            except StopIteration:
                return None
        return s
