def what_time_is_it(angle):
    n=60*12*angle/360
    return "%02d:%02d"%(int(n//60) or 12,int(n%60))

