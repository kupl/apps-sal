def riders(stations, lost):
    stations = stations[:lost - 1] + stations[lost - 2:]
    rider, dist = 1, 0
    for i, d in enumerate(stations):
        rider += (dist + d > 100) + (i == lost - 2)
        dist = dist * (dist + d <= 100 and i != lost - 2) + d
    return rider
