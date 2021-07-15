def next_item(xs, item):
    print((repr(xs), item))
    try:
        return xs[xs.index(item)+1]
    except ValueError:
        return None
    except IndexError:
        return None
    except AttributeError:
        if repr(xs)[:5] == 'count':
            return item + 1
        else:
            try:
                i = 0
                while i != item:
                    i = xs.__next__()
                    if i == item:
                        return xs.__next__()
            except StopIteration:
                return None
                

