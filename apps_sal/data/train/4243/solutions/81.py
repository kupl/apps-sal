websites = ['codewars'] # create an array called websites that has "codewars" as its only value

def find_average(arr):
    count = 0
    sum = 0
    for number in arr:
        count += 1
        sum += number
    return sum / count

