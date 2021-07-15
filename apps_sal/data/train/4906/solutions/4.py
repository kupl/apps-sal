def traffic_lights(road, n):

    print(road)
    index_red_init = [i for i,j in enumerate(road) if j =='R']
    index_green_init = [i for i,j in enumerate(road) if j =='G']
    index_orange_init = [i for i,j in enumerate(road) if j =='O']
    print(index_green_init)
    #print(type(road))
    road_lst = [i for i in road]

    red_init = 'RRRRRGGGGGO'
    green_init = 'GGGGGORRRRR'
    orange_init = 'ORRRRRGGGGG'
    
    index_car = 0
    
    time = 0
    count = 0
    car_index = -1
    final = []
    while time <= n and car_index <= len(road) - 1:
        
        #if car_index == len(road) - 1:
            
        
        if count >= len(red_init):
            count = count - len(red_init)
        for i in index_red_init:
            road_lst[i] = red_init[count]
        for i in index_green_init:
            road_lst[i] = green_init[count]
        for i in index_orange_init:
            road_lst[i] = orange_init[count]
        
        #print(car_index + 1)
        
        if car_index != len(road) - 1:
        
            if road_lst[car_index + 1] == 'R':
                car_index = car_index
            elif road_lst[car_index + 1] == 'O':
                car_index = car_index
            else:
                car_index += 1
            road_lst[car_index] = 'C'
        elif road[-1] == 'R':
            road_lst[-1] = red_init[count]
        elif road[-1] == 'G':
            road_lst[-1] = green_init[count]
        elif road[-1] == 'O':
            road_lst[-1] = orange_init[count]
        else:
            road_lst[-1] = '.'
            
        

        if car_index - 1 in index_red_init:
            road_lst[car_index - 1] = red_init[count]
        elif car_index - 1  in index_green_init:
            road_lst[car_index - 1] = green_init[count]
        elif car_index - 1  in index_orange_init:
            road_lst[car_index - 1] = orange_init[count]
        elif car_index - 1 >= 0:
            road_lst[car_index - 1] = '.'
            
        result = ''.join(road_lst)

        final.append(result)
        count += 1
            
        time += 1
    
    return final
