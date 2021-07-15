def rental_car_cost(d):
    if 0 < d < 3: return 40*d
    if 2 < d < 7: return 40*d - 20
    if d > 6: return 40*d - 50
    
    
    
# Every day you rent the car costs $40.
# If you rent the car for 7 or more days,
# you get $50 off your total. 
# Alternatively, if you rent the car for 3 or more days,
# you get $20 off your total.

# Write a code that gives out the total amount for different days(d).


