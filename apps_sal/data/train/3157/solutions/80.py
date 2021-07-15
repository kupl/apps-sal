def number(bus_stops):
    ans = 0
    for o in bus_stops:
        ans += o[0]
        ans -= o[1]
    return ans
