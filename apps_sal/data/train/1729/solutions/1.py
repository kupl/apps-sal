import re

facing = 0                                                                  # directions - [0,1,2,3]
current_position = [0, 0]

def i_am_here(path):
    nonlocal current_position, facing
                                                                            
    movement_dict = {'r':1, 'l':-1, 'R':2, 'L':-2}                          # used to update the facing direction  
    walk_direction = {0: (-1, 0),1: (0, 1),2: (1, 0),3: (0, -1)}            # used to walk in the facing direction
    
    for l in re.findall('\d+|\D', path):
        if l.isalpha():
            facing = (facing + movement_dict[l]) % 4
        else:
            no_of_steps = int(l)
            current_position[0] += walk_direction[facing][0] * no_of_steps
            current_position[1] += walk_direction[facing][1] * no_of_steps
            
    return current_position
