from datetime import timedelta


def solve(arr):
    max = 0
    a = list(dict.fromkeys(arr))  # Used to remove duplicate times
    new_list = []
    if len(a) > 1:
        for i in enumerate(a):  # Numbered iteration though List a
            new_list.append(str(i[1].replace(":", "")))
        new_list.sort()  # Chronologically ordered alarm times
        new_list.reverse()  # From highest to lowest

        for i in enumerate(new_list):  # numbered list to make further code simpler/more organised
            if i[0] <= (len(new_list) - 2):
                delta_hours = int((i[1])[:2:]) - int((new_list[i[0] + 1])[:2:])  # This prepares the hour difference for the timedelata function later
                delta_mins = int((i[1])[2::]) - int((new_list[i[0] + 1])[2::]) - 1  # This prepares the minutes difference for the timedelata function later
                t = (str(timedelta(hours=delta_hours, minutes=delta_mins)))[:-3]  # This calculates the time difference between the time increments in the list
                c = int(t.replace(":", ""))  # Eliminates the colon and turns the time into a integer so that the largest time can be determined
                if c >= max:  # If the time value is larger than the previous values of c, this becomes the new value of c
                    max = c
                    result = t

            if i[0] == (len(new_list) - 1):
                loop_hrs = int((i[1])[:2:]) - int((new_list[0])[:2:]) + 24  # This determienes the hour differnece between alarms in different days (PM->AM)
                loop_mins = int((i[1])[2::]) - int((new_list[0])[2::]) - 1  # This determienes the minute differnece between alarms in different days (PM->AM)
                d = (str(timedelta(hours=loop_hrs, minutes=loop_mins)))[:-3]
                c = int(d.replace(":", ""))
                if c >= max:  # If this time interval is greater than the previous time intervals, it becomes the new c value
                    result = d

        if len(result) == 4:  # Time delta may only have one hour value, if this is the case, add 0 to the interval string to ensure a 5 character time interval
            result = "0" + result
        return(result)  # Return the result

    else:
        return("23:59")  # In the event that there is only one alarm, this will always be the time interval so return this
