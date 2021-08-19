def longest(s1, s2):
    # your code
    distinct = set(s1 + s2)  # sets are distinct values!
    distinctSorted = sorted(distinct)  # turn into sorted list
    return ''.join(distinctSorted)  # concatenate to string with 'join'
