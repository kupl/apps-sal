def sort_array(lst):
    (even, odd) = ([], [])
    for n in sorted(lst):
        (odd if n & 1 else even).append(n)
    (even, odd) = (iter(even[::-1]), iter(odd))
    return [next(odd if n & 1 else even) for n in lst]
