from datetime import datetime, timedelta

def bus_timer(current_time):
    
    ct = datetime.strptime(current_time, "%H:%M")
    
    if ct >= datetime.strptime("5:55", "%H:%M") and ct <= datetime.strptime("23:55", "%H:%M"):
        if ct.minute <= 10:
            time_left = 10 - ct.minute
        elif ct.minute <= 25 and ct.minute > 10:
            time_left = 25 - ct.minute
        elif ct.minute <= 40 and ct.minute > 25:
            time_left = 40 - ct.minute
        elif ct.minute <= 55 and ct.minute > 40:
            time_left = 55 - ct.minute
        else:
            time_left = 70 - ct.minute
    else:
        delta = datetime.strptime("5:55", "%H:%M") - ct
        time_left = int(delta.seconds / 60)
            
    return time_left
