def number(bus_stops):
    try:
        last_passengers = 0
        total_people_in = 0
        total_people_out = 0
        for (first_item, second_item) in bus_stops:
            total_people_in += first_item
            total_people_out += second_item
    except:
        print('Uh oh! Something went really wrong!')
        quit
    finally:
        last_passengers = total_people_in - total_people_out
        if last_passengers >= 0:
            print('Remaining Passengers for last stop: ', last_passengers)
            return last_passengers
        else:
            print('No passengers where on the bus')
            last_passengers = 0
            return last_passengers
