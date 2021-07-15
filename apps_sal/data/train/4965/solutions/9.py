def sum_of_integers_in_string(s):
    for x in s: 
        if not x.isdigit(): s = s.replace(x, ' ')
    return sum(map(int, s.split()))
