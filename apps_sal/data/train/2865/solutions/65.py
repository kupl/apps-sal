def solution(string):
    # turn string to list
    list1 = list(string)
    # reverse list
    reverse1 = reversed(list1)
    # returned list to string with join
    reversed_string = ''.join(reverse1)
    return reversed_string
