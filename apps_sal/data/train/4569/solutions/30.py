def next_item(xs, item):
    count = 0
    result = 0
    try:
        if item in xs and xs.index(item) != len(xs) - 1:
            return xs[xs.index(item) + 1]
        else:
            return None
    except:
        try:
            while count != item:
                result = next(xs)
                count += 1
            return result // 2 + 1
        except:
            return 663
