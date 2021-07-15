import sys
def difference_in_ages(ages):
    # your code here
    array = []
    youngest = sys.maxsize
    oldest = -sys.maxsize - 1
    for i in ages:
        if youngest > i:
            youngest = i
        if oldest < i:
            oldest = i
    difference = oldest - youngest

    return (youngest, oldest, difference)
