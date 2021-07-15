def number(bus_stops):
    number_of_people = 0
    for i in bus_stops:
        number_of_people += i[0]
        number_of_people -= i[1]
    return number_of_people    
