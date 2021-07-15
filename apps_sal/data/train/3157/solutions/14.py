def number(bus_stops):
    total_number = 0
    for i in bus_stops:
        total_number += i[0] - i[1]
        
    return total_number
    

