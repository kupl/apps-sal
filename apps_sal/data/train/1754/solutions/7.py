def valid(a):
    golfers = {}
    for i in a:
        for j in i:
            for k in j:
                golfers[k] = []
    for days in a: 
        for group in days:
            for person in golfers:
                if person in group:
                    for people in group:
                        if person != people:
                            if people in golfers[person]:
                                return False
                            golfers[person] += people
    length = len(golfers["A"])
    for i in golfers:
        if len(golfers[i]) != length:
            return False
    return True

