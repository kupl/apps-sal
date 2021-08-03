def bad_apples(apples):
    packed = []
    while apples:
        package = apples.pop(0)
        if min(package) > 0:
            # Both apples are positive
            packed.append(package)
        elif max(package) == 0:
            # Both apples are rotten
            continue
        else:  # Only one good apple
            # Filter for other packs with one good apple
            singles = filter(lambda x: min(x) == 0 and max(x) > 0, apples)
            try:
                # Try to get the next filtered package
                next_single = next(singles)
                # If found, remove from remaining apples and repackage
                apples.remove(next_single)
                packed.append([max(package), max(next_single)])
            except StopIteration:
                # If not found, discard and do nothing
                pass
    return packed
