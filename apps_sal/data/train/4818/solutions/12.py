def solution(a, b):
    shortest_string = None
    longest_string = None
    if min(len(a), len(b)) == len(a):
        shortest_string = a
        longest_string = b
    else:
        shortest_string = b
        longest_string = a
    return shortest_string + longest_string + shortest_string
