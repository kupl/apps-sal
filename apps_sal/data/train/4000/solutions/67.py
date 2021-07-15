from math import factorial as f
def strong_num(number):
    number = str(number)
    strong = sum([f(int(x)) for x in number])
    return "STRONG!!!!" if strong == int(number) else "Not Strong !!"
