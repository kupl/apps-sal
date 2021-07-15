import math
def get_average(marks):
    res=sum(marks)/len(marks)
    return math.ceil(res) if math.ceil(res)<math.floor(res) else math.floor(res)

