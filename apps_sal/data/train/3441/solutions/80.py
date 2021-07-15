import math
def get_average(marks):
    soma = 0
    
    if (len(marks)>0):
        for i in marks:
            soma += i
    
        media = soma/len(marks)
        return math.floor(media)

print (get_average([1,2,15,15,17,11,12,17,17,14,13,15,6,11,8,7]))
