def start_smoking(bars, boxes):
    cigarettes = bars * 10 * 18 + boxes * 18
    smoked = 0
    leftovers = 0
    while True:
        smoked += cigarettes
        leftovers += cigarettes
        cigarettes = 0
        if leftovers >= 5:
            cigarettes += leftovers // 5
            leftovers = leftovers % 5
        else:
            return smoked
