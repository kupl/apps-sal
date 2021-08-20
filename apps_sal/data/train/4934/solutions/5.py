def sort(words):
    if not words:
        return
    it = iter(words)
    pivot = next(it)
    (lt, ge) = ([], [])
    for i in it:
        if i < pivot:
            lt.append(i)
        else:
            ge.append(i)
    yield from sort(lt)
    yield pivot
    yield from sort(ge)
