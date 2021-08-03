def next_item(xs, item=None):
    try:
        a = xs.index(item)
        return xs[a + 1]
    except ValueError:
        return None
    except IndexError:
        pass
    except AttributeError:
        if item in xs:
            return next(xs)
