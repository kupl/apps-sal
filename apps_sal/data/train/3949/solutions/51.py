import math
def calculate_tip(amount, rating):
    #your code here
    c=rating.capitalize()
    if(c=="Poor" or "Terrible" or "Good" or "Great" or "Excellent" ):
        if(c=="Poor"):
            return math.ceil(amount*(5/100))
        elif(c=="Excellent"):
            return math.ceil(amount*(20/100))
        elif(c=="Great"):
            return math.ceil(amount*(15/100))
        elif(c=="Good"):
            return math.ceil(amount*(10/100))
        elif(c=="Terrible"):
            return 0
    return 'Rating not recognised'
