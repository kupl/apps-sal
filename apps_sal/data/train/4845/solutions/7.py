from copy import deepcopy


def sort_nested_list(a):

    def seeker(lst):
        return lst if not lst or not isinstance(lst[0], list) else sum(map(seeker, lst), [])

    def putter(lst):
        for i in range(len(lst)):
            if isinstance(lst[i], list):
                putter(lst[i])
            else:
                lst[i] = next(elts)
    (a, elts) = (deepcopy(a), iter(sorted(seeker(a))))
    putter(a)
    return a
