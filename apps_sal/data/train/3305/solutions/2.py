def shortest(N, edgeList):
    
    edgeList.sort(key= lambda x: x[0])
    path_values = [None for _ in range(N)]
    path_values[0] = 0
        
    for edge in edgeList:

        if path_values[edge[0]] != None: # If the node value is 0, then we can not use it as a base to go further.
            new_val = edge[2] + path_values[edge[0]]
        
            if path_values[edge[1]] == None:
                path_values[edge[1]] = new_val
            else:
                path_values[edge[1]] = min(path_values[edge[1]], new_val)
    
    if path_values[-1] == None: # no path goes to the end
        return -1
    else:
        return path_values[-1]
