# https://www.codewars.com/kata/shortest-knight-path/python

# Function to transform from "a1" to "[1,1]", for example
def transformChessPointToMatrixPoint(point):
    return [int(ord(point[0]) - 96), int(point[1])]

# From a point in a matrix, check all possible moves as a knight and then remove every move out of the board.


def availableMoves(point):
    moves = []
    final_moves = []
    moves.append([point[0] + 2, point[1] + 1])
    moves.append([point[0] + 2, point[1] - 1])
    moves.append([point[0] - 2, point[1] + 1])
    moves.append([point[0] - 2, point[1] - 1])
    moves.append([point[0] + 1, point[1] + 2])
    moves.append([point[0] + 1, point[1] - 2])
    moves.append([point[0] - 1, point[1] + 2])
    moves.append([point[0] - 1, point[1] - 2])

    # Return only the points IN the board
    for move in moves:
        if 1 <= move[0] <= 8 and 1 <= move[1] <= 8:
            final_moves.append(move)
    return final_moves

# Main Function - Implementing Breadth First Search (kinda)


def knight(p1, p2):
    # Transform Points from letters "ky" to "[x,y]" points
    p1 = transformChessPointToMatrixPoint(p1)
    p2 = transformChessPointToMatrixPoint(p2)
    # Initialize visited nodes
    already_visited = [p1]

    # Queue to check and to find the minimum solution. A list of arrays where first is the point (array [x,y]) and second is the amount of steps done, initialized at 0.
    to_check = [[p1, 0]]

    # While we have nodes to check
    while len(to_check) > 0:

        # If we have found the answer
        if to_check[0][0] == p2:
            # Return the amount of steps done
            return to_check[0][1]

        # Check available moves from point to_check[0][0]
        moves_to_visit = availableMoves(to_check[0][0])
        for move in moves_to_visit:
            # If they have been visited once, we must not check them again
            if move in already_visited:
                pass
            # First time checking the point
            else:
                # Added to visited nodes
                already_visited.append(move)
                # Added to the check "queue" and added 1 to the amount of steps
                to_check.append([move, to_check[0][1] + 1])
        # Remove first node after being checked
        to_check.pop(0)
    # Return impossibility to reach an answer (just in case they enter an invalid point out of an 8x8 board)
    return None
