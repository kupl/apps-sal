def index(array, n):
    nth_power = None
    try: nth_power = array[n]**n
    except: nth_power = -1
    return nth_power
