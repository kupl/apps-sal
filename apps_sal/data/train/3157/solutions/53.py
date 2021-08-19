def number(bus_stops):
    try:
        last_passengers = sum((people_in - people_out for (people_in, people_out) in bus_stops))
    except:
        print('Uh oh! Something went really wrong!')
        quit
    finally:
        if last_passengers >= 0:
            print('Remaining Passengers for last stop: ', last_passengers)
            return last_passengers
        else:
            print('No passengers where on the bus')
            last_passengers = 0
            return last_passengers
