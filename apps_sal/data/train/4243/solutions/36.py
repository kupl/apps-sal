# create an array called websites that has "codewars" as its only value
def find_average(num):
    sum = 0
    for i in num:
        sum += i
        average = sum/len(num)
    return average

