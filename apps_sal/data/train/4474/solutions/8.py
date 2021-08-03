def start_smoking(bars, boxes):
    cigarettes = bars * 10 * 18 + boxes * 18
    smoked = 0
    leftovers = 0
    # Tenemos esa cantidad de cigarrillos los fumamos nos quedamos sin cigarrillos:
    while True:
        smoked += cigarettes
        leftovers += cigarettes
        cigarettes = 0
        # Entonces  ahora tenemos que usar los leftovers
        if leftovers >= 5:
            cigarettes += leftovers // 5
            leftovers = leftovers % 5
        else:
            return smoked
