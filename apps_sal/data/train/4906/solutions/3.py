def light_changes_iter(n, *args):
    '''
    n - no. iterations
    args is a pattern in a form of tuple
    stores the iterations where lights must be changed
    '''
    iteration = 0
    tup = () 
    while True:
        for x in args:
            iteration += x
            tup += (iteration,) #append tuple
            if max(tup) > n:
                return tup[:-1] #pop out last element, it is above last iteration

def shift_lights(road_state, init_state):
    '''
    current road_state
    initial_state - list with the indexes of the initial light state
    current_pos - current position of the car to be updated
    pos_index - position of the car
    '''
    temp = road_state.split(" ") #string to list
    
    #only updates the positions correspondent to the initial signal
    #change current_pos if the car is in the same position as a signal
    for index in init_state: 
        if temp[0][index] == "O":
            temp[0] = temp[0][:index] + "R" + temp[0][index+1:]

        elif temp[0][index] == "G":
            temp[0] = temp[0][:index] + "O" + temp[0][index+1:]

        elif temp[0][index] == "R":
            temp[0] = temp[0][:index] + "G" + temp[0][index+1:]

    return "".join(temp)
 
def traffic_lights(road_state, n):
    '''
    road_state is a list with the initial road state
    '''
    road = [] + [road_state] #store road progress in a list
    road_simulated = "." + road_state[1:] #simulates road without car
    
    #iterations where light changes if position starts with green, orange, red
    green = light_changes_iter(n, 5,1,5)
    orange = light_changes_iter(n, 1,5,5) 
    red = light_changes_iter(n, 5,5,1)

    #store the indexes of initial states of the lights to keep track 
    #how they should change across iterations
    init_green = [i for i,char in enumerate(road_simulated) if char == "G"]
    init_orange = [i for i,char in enumerate(road_simulated) if char == "O"]
    init_red = [i for i,char in enumerate(road_simulated) if char == "R"]
    
    #start variables
    pos_index = 0 #current position of the car

    for ite in range(1,n+1):
        #update lights according to iteration
        if ite in green:
            road_simulated = shift_lights(road_simulated, init_green)
        if ite in orange:
            road_simulated = shift_lights(road_simulated, init_orange)
        if ite in red:
            road_simulated = shift_lights(road_simulated, init_red)
        
        try:
            #check if car should stop
            if road_simulated[pos_index + 1] in ("O", "R"):
                road_state = road_simulated[:pos_index] + "C" + road_simulated[pos_index+1:]
                road.append(road_state)
                continue
            
            #move the car
            pos_index += 1
            road_state = road_simulated[:pos_index] + "C" + road_simulated[pos_index+1:]
            road.append(road_state)
    
        except IndexError: #last iteration, car goes out of road
            road.append(road_simulated)  
        
    return road

