def disarium_number(number):
    digits = [int(d) for d in str(number)]
    
    dis_calc=0
    
    for i,d in enumerate(digits):
        dis_calc+=d**(i+1)
    
    return "Disarium !!" if dis_calc==number else "Not !!"
