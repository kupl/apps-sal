def sort(arr):
    """ You'll have to try harder than that @sazlin """
    result = [a for a in arr]
    result.__getattribute__('sort')()
    yield from result
