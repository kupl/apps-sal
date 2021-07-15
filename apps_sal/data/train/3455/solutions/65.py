def disarium_number(number):
    
    return "Disarium !!" if sum([int(e) ** c for c,e in enumerate(str(number),1)]) == number else "Not !!" 
