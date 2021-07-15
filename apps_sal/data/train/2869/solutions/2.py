# Using Set:
# Time complexity | O(N)
def distinct(seq):
    result = []
    seen = set()
    for a in seq:   #O(N) operation in terms of time complexity
        if a not in seen:  #O(1) operation in terms of time complexity
            result.append(a)
            seen.add(a)
    return result

