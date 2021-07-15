def longest(s1, s2):
    new_string = set(s1 + s2)
    sort_string = sorted(new_string)
    return "".join(s for s in sort_string)
    
    # your code

