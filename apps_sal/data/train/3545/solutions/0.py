from itertools import chain

def well(arr):
    c = sum(isinstance(x, str) and x.lower() == 'good' for x in chain.from_iterable(arr))
    return (
        'I smell a series!' if c > 2 else
        'Publish!' if c > 0 else
        'Fail!'
    )
