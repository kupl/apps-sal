def zero_fuel(distance_to_pump, mpg, fuel_left):
    if (distance_to_pump / mpg) - fuel_left <= 0:
        ergebnis = True
    else:
        ergebnis = False
    return ergebnis


print((zero_fuel(50, 25, 2)))
print((zero_fuel(100, 50, 1)))
