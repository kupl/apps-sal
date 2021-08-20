def is_odd_heavy(a):
    return max([n for n in a if -~n % 2] or [float('-inf')]) < min([n for n in a if n % 2] or [float('-inf')])
