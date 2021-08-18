def number(bus_stops):
    '''
    input: bus_stops tuple - the 
    approach: loop through and sum the first element and sum the last element then subtract the two numbers
    output: the 
    '''
    passengersOn = 0
    passengersOff = 0

    try:
        res = sum(i[0] for i in bus_stops) - sum(i[1] for i in bus_stops)

    except:
        print("There was an error")

    return res
