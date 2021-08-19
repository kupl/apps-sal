import copy


def find_solution(puzzle):
    moveset = []
    while True:
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
    if move < len(puzzle):
        for i in puzzle[move]:
            count += 1 if i == 0 else 0
    else:
        index = move - len(puzzle)
        for row in puzzle:
            count += 1 if row[index] == 0 else 0
    return count


'\n# Use BFS?\ndef find_solution(puzzle):\n    fringe = [([], puzzle)]\n    while (True): # We should always find a solution for any configuration?\n        \n        (moveset, current_state) = fringe.pop()\n        \n        # Test if current state is a solution\n        valid = True\n        for x in range(len(current_state)):\n            if 0 in current_state[x]:\n                valid = False\n                break\n        if valid:\n            return moveset\n        \n        # If state is not solution then we generate successor states add to fringe queue\n        successors = generate_successors(moveset, current_state)\n        for s in successors:\n            fringe.insert(0, s)\n            \n    \n    \n# This function takes a moveset and a puzzle and returns all the possible successors for that puzzle\ndef generate_successors(move_list, puzzle):\n    successors = []\n    for x in range(len(puzzle) * 2):\n        \n        new_state = copy.deepcopy(puzzle)\n        new_move_list = move_list[:]\n        new_move_list.append(x)\n        \n        # If x < len(puzzle) we toggle a row\n        if x < len(puzzle):\n            new_state[x] = [1 if y == 0 else 0 for y in new_state[x]]\n            successors.append((new_move_list, new_state))\n        \n        # Else toggle column\n        else:\n            index = x - len(puzzle)\n            for i in range(len(puzzle)):\n                new_state[i][index] = 0 if new_state[i][index] == 1 else 1\n            successors.append((new_move_list, new_state))\n            \n    return successors\n'
