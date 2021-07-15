def traffic_jam(main_road, side_streets):
    #display(main_road, side_streets)
    
    result = ''
    
    while True:
        for i in range(len(main_road) - 1, -1, -1):
            if len(side_streets) > i and len(side_streets[i])> 0:
                main_road = main_road[:i+1] + side_streets[i][-1] + main_road[i+1:]
                side_streets[i] = side_streets[i][:-1]
                side_streets = side_streets[:i] + [''] + side_streets[i:]
        result += main_road[0]
        if main_road[0] == 'X':
            return result
        main_road = main_road[1:]

