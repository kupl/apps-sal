import math
def cost(mins):
    return 30 if mins<60 else math.ceil(((mins-60)-5)/30)*10+30

