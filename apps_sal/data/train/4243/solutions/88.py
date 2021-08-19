# create an array called websites that has "codewars" as its only value
def find_average(websites):
    count = 0
    for i in websites:
        count += i
    return count // len(websites)
