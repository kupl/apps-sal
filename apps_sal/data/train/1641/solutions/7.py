from itertools import zip_longest


def normalize(lst: List, growing: int = 0) -> List:
    """Convert the given nested list to hypercube format with the given <growing_value> and return it.
    """

    def seeker(lst, d=1):
        yield (len(lst), d)
        for elt in lst:
            if isinstance(elt, list):
                yield from seeker(elt, d + 1)

    def grower(lst, d=1):
        return [grower(o if isinstance(o, list) else [o] * size, d + 1) if d != depth else o for (o, _) in zip_longest(lst, list(range(size)), fillvalue=growing)]
    (size, depth) = list(map(max, list(zip(*seeker(lst)))))
    return grower(lst)
