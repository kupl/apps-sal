def bad_apples(apples):
    packed = []
    while apples:
        package = apples.pop(0)
        if min(package) > 0:
            packed.append(package)
        elif max(package) == 0:
            continue
        else:
            singles = filter(lambda x: min(x) == 0 and max(x) > 0, apples)
            try:
                next_single = next(singles)
                apples.remove(next_single)
                packed.append([max(package), max(next_single)])
            except StopIteration:
                pass
    return packed
