import math
def calculate_tip(amount, rating):
    legend=[("terrible",0),("poor",5),("good",10),("great",15),("excellent",20)]
    for i in range (len(legend)):
        if rating.lower()==legend[i][0]:
            return math.ceil(amount*legend[i][1]/100)
        else:
            pass
    return "Rating not recognised"

