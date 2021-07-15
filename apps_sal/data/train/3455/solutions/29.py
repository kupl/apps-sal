def disarium_number(number):
    return "Disarium !!" if number==sum([int(x)**(i+1) for i,x in enumerate(str(number))]) else "Not !!"
