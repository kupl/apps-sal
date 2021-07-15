def traffic_jam(main_road, side_streets):
    
    road = list(main_road)
    indice = road.index('X')
    road = road[:indice+1]
    
    side = [list(e) for e in side_streets]
    if not side : return ''.join(road)
    
    if len(side)<len(road):
        side += [[] for k in range(len(road)-len(side)) ]

    final = []
    def conduit(voiture, position):
        while position>0:
            if side[position-1]:
                v = side[position-1].pop()
                conduit(v, position-1)
            position -=1
        final.append(voiture)
    
    for i, voiture in enumerate(road):
        conduit(voiture, i)
    
    return ''.join(final)
