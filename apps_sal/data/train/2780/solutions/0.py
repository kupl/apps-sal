def time(distance,boat_speed,stream):
    return round(distance/(boat_speed+int(stream.split()[-1])),2) if stream[0]=="D" else round(distance/(boat_speed-int(stream.split()[-1])), 2)
