import math

def get_average(marks):
    number = len(marks)
    total = 0
    
    
    for student in marks:
        total = total + student
        
    return math.floor(total/number)
        

