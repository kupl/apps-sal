import math
def get_average(marks):
    count=0
    sum=0
    for x in marks:
        sum+=x
        count+=1
    return math.floor(sum/count)

