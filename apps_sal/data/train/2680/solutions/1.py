from datetime import datetime, timedelta

def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        sec = timedelta(seconds=int((g*3600/(v2-v1))))
        d = datetime(1,1,1) + sec
        
        return [d.hour, d.minute, d.second]
