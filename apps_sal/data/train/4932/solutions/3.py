import copy


def find_solution(puzzle):
    moveset = []
    while(True):
        # Find first rows with most 0's
        move_to_exe = 0
        max_zeros = 0
        for i in range(len(puzzle) * 2):
            score = count_zeros(i, puzzle)
            if score > max_zeros:
                max_zeros = score
                move_to_exe = i
        if max_zeros == 0:
            return moveset
        moveset.append(move_to_exe)
        if move_to_exe < len(puzzle):
            puzzle[move_to_exe] = [0 if y == 1 else 1 for y in puzzle[move_to_exe]]
        else:
            index = move_to_exe - len(puzzle)
            for i in range(len(puzzle)):
                puzzle[i][index] = 0 if puzzle[i][index] == 1 else 1


def count_zeros(move, puzzle):
    count = 0
    # Row toggle
    if move < len(puzzle):
        for i in puzzle[move]:
            count += 1 if i == 0 else 0
    else:
        index = move - len(puzzle)
        for row in puzzle:
            count += 1 if row[index] == 0 else 0
    return count

# UGH that solution is so BASIC! Greedy execution? Lame. I perfer the BF tree search below.


"""
# Use BFS?
def find_solution(puzzle):
    fringe = [([], puzzle)]
    while (True): # We should always find a solution for any configuration?
        
        (moveset, current_state) = fringe.pop()
        
        # Test if current state is a solution
        valid = True
        for x in range(len(current_state)):
            if 0 in current_state[x]:
                valid = False
                break
        if valid:
            return moveset
        
        # If state is not solution then we generate successor states add to fringe queue
        successors = generate_successors(moveset, current_state)
        for s in successors:
            fringe.insert(0, s)
            
    
    
# This function takes a moveset and a puzzle and returns all the possible successors for that puzzle
def generate_successors(move_list, puzzle):
    successors = []
    for x in range(len(puzzle) * 2):
        
        new_state = copy.deepcopy(puzzle)
        new_move_list = move_list[:]
        new_move_list.append(x)
        
        # If x < len(puzzle) we toggle a row
        if x < len(puzzle):
            new_state[x] = [1 if y == 0 else 0 for y in new_state[x]]
            successors.append((new_move_list, new_state))
        
        # Else toggle column
        else:
            index = x - len(puzzle)
            for i in range(len(puzzle)):
                new_state[i][index] = 0 if new_state[i][index] == 1 else 1
            successors.append((new_move_list, new_state))
            
    return successors
"""
