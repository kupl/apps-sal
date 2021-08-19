def number(bus_stops):
    # Good Luck!
    '''
    input: bus_stops tuple - the # of people who get on and off the bus
    approach: loop through and sum the first element and sum the last element then subtract the two numbers
    output: the # of people left on the bus after the last stop
    '''
    passengersOn = 0
    passengersOff = 0

    try:
        res = sum(i[0] for i in bus_stops) - sum(i[1] for i in bus_stops)

    except:
        print("There was an error")

    return res
