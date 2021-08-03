# create an array called websites that has "codewars" as its only value
def find_average(lst):
    sum = 0
    for i in lst:
        sum += i
    return int(sum / len(lst))
