def is_sorted_and_how(a): return ['no', 'yes, ascending', 'yes, descending'][(sorted(a) == a) + (sorted(a)[::-1] == a) * 2]
