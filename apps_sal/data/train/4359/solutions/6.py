def cube_times(times):
    times.sort()
    a= [0,0]
    a[0] = round((float(times[1]) + float(times[2]) + float(times[3]))/3,2)
    a[1] = times[0]
    return tuple(a)
    

