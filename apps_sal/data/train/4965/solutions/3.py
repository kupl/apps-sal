def sum_of_integers_in_string(s):
    return sum(map(int, ''.join(c if c.isdigit() else ' ' for c in s).split()))
