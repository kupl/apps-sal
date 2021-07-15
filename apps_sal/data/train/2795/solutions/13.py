def cockroach_speed(s):
    '''
    (number) -> int
    s is the number of kilometers that the cockroach travels per hour. 
    Return the equivalent integer(rounded down) of centimeters per second.
    '''
    #convert kilometer(per hour) to centimeters(per hour)
    #convert centimeters(per hour) to centimeters(per second)
    #convert the final result as an integer.
    return int((s * 100000) // 3600)
    

