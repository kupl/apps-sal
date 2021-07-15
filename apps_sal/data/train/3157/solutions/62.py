def number(bus_stops):
    solut = 0
    for x in bus_stops:
        solut += x[0]
        solut -= x[1]
    return solut
