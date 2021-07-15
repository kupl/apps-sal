def find_next_bridge_end(position, terrain):
    next_bridge_end_position = ''.join(terrain[position:]).find('---')
    if next_bridge_end_position == -1:
        return len(terrain)+1
    
    return next_bridge_end_position + position
    
def check_if_bridge_position(i, terrain):
    if i == 0:
        previous_terrain = '-'
        next_terrain = terrain[i+1]
    elif i >= len(terrain)-1:
        previous_terrain = terrain[i-1]
        next_terrain = '-'
    else:
        previous_terrain = terrain[i-1]
        next_terrain = terrain[i+1]

    if previous_terrain == '-' and terrain[i] == '-' and next_terrain == '-':
        return False
    return True

def create_terrain_with_ants(ant_positions, terrain):
    terrain_with_ants = terrain[:]
    for ant, position in list(ant_positions.items()):
        terrain_with_ants[position] = ant
    return ''.join(terrain_with_ants)

def ant_bridge(ants, terrain):
    platform = ''.join(['-' for _ in range(len(ants))])
    terrain = platform + terrain + platform
    terrain = list(terrain)
    terrain_length = len(terrain)
    
    ant_positions = list(range(len(ants)))

    print(ants)
    print((''.join(terrain)))

    initial_states = []
    
    if len(ants) >= len(terrain):
        return ants
    
    for i in range(len(ants)):
        if i <= 0:
            previous_terrain = '-'
            current_terrain = terrain[i]
            next_terrain = terrain[i+1]
        elif i >= len(terrain)-1:
            previous_terrain = terrain[i-1]
            current_terrain = terrain[i]
            next_terrain = '-'
        else:
            previous_terrain = terrain[i-1]
            current_terrain = terrain[i]
            next_terrain = terrain[i+1]
            
        if not previous_terrain == '.' and current_terrain == '-' and not next_terrain == '.':
            initial_states.append('')
        else:
            initial_states.append('b')
    
    ant_states = dict(list(zip(ants, initial_states)))
    ant_positions = dict(list(zip(ants[::-1], list(range(len(ants)-1, -1, -1)))))
    
    for k in range(len(ants), terrain_length):
        #print("Iteration " + str(k))
        max_ant_position = max(ant_positions.values())
        min_ant_position = min(ant_positions.values())
    
        #print(create_terrain_with_ants(ant_positions, terrain))
    
        for ant in ants:
            i = ant_positions[ant]
            s = ant_states[ant]
        
            is_end_of_terrain_reached = i >= len(terrain)-2
        
            if is_end_of_terrain_reached:
                terrain = terrain + ['-', '-']

            # ant is not part of a bridge and next position cannot be part of a bridge => increment by 1    
            if terrain[i] == '-' and terrain[i+1] == '-' and terrain[i+2] == '-' and s == '':
                ant_positions[ant] = i+1
                ant_states[ant] = ''
            # ant is not part of a bridge and it is at the front of the queue and next position is start of a bridge => increment by 1 and start a bridge
            if terrain[i] == '-' and terrain[i+1] == '-' and terrain[i+2] == '.' and s == '' and i == max_ant_position:
                ant_positions[ant] = i+1
                ant_states[ant] = 'b'     
            # ant is not part of a bridge and it is not at the front of the queue and next position is start of a bridge => jump ahead to the front of the queue
            if terrain[i] == '-' and terrain[i+1] == '-' and terrain[i+2] == '.' and s == '' and not i == max_ant_position:
                # DUPLICATED CODE
                next_bridge_end = find_next_bridge_end(i, terrain)
                if next_bridge_end < max_ant_position:
                    ant_positions[ant] = next_bridge_end + 1
                else:           
                    ant_positions[ant] = max_ant_position + 1
                ant_states[ant] = ''
                if check_if_bridge_position(ant_positions[ant], terrain):
                    ant_states[ant] = 'b'      
            # ant is part of a bridge and it is at the back of the queue => jump ahead to the next bridge end or to the front of the queue
            if s == 'b' and i == min_ant_position:
                next_bridge_end = find_next_bridge_end(i, terrain)
                if next_bridge_end < max_ant_position:
                    ant_positions[ant] = next_bridge_end + 1
                else:           
                    ant_positions[ant] = max_ant_position + 1
                
                ant_states[ant] = ''
                if check_if_bridge_position(ant_positions[ant], terrain):
                    ant_states[ant] = 'b'
            
            if is_end_of_terrain_reached:
                terrain = terrain[:len(terrain)-2]
            
            #print(create_terrain_with_ants(ant_positions, terrain))      
    
    return ''.join(sorted(ant_positions, key=ant_positions.get))

