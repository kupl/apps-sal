from math import ceil

d = {
    "terrible":0, "poor":5, "good":10, "great":15, "excellent":20    
}

def calculate_tip(amount, rating):
    #your code here
    rating = rating.lower()
    if rating not in d.keys():
        return 'Rating not recognised'
    else:
        return ceil(amount*d[rating]/100)
