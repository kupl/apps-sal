import math
def cost(mins):
    
    if mins <= 60:
        return 30
    
    if mins > 60:
        if (mins % 30) <= 5:
            leftover = mins - 60
            multiple = round(leftover / 30)
            return 30 + (10 * (multiple))
        
        if (mins % 30) > 5:
            leftover = mins - 60
            multiple = math.ceil(leftover/30)
            return 30 + (10 * multiple)

