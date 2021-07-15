'''
Vasyl Zakharuk
Python Core 355
Codewars Kata: Will you make it?
''' 
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if fuel_left >= distance_to_pump / mpg:
        print("We got to the pump")
        return True
    else:
        print("We pushed the car to the pump(((")
        return False
print(zero_fuel(50,25,2))
