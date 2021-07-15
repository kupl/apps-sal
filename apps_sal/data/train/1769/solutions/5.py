def shortestPath(topology, startPoint, endPoint):
    print(topology)
    print(startPoint)
    print(endPoint)

    visitedNodes = {}; #node name, node path
    boarderNodes = {startPoint:{'path': [[startPoint]], 'cost':0}}; #node name, node path, node cost
    
    #do greedy first search
    #loop while boarder not empty
    while(len(boarderNodes)>0):
        #expand unknown node with lowest cost
        cost = None
        node = ''
        for boarderNodeName, boarderNodeDict in list(boarderNodes.items()):
            if(cost == None):
                node = boarderNodeName
                cost = boarderNodeDict['cost']
            elif(boarderNodeDict['cost']<cost):
                node = boarderNodeName
                cost = boarderNodeDict['cost']
                
        path = boarderNodes[node]['path']
        visitedNodes[node] = path
        del boarderNodes[node]
        
        # add to boarder at right spot/ update cost values if necessary
        for neighborNode, neighborCost in list(topology[node].items()):
            if (not neighborNode in visitedNodes)and(not neighborNode in boarderNodes):
                boarderNodes[neighborNode] = {'path': [[]] ,'cost': cost+neighborCost}
                addPath(boarderNodes,neighborNode,path)
            elif (not neighborNode in visitedNodes)and(neighborNode in boarderNodes):
                if(boarderNodes[neighborNode]['cost'] > cost+neighborCost):
                    boarderNodes[neighborNode]['cost'] = cost+neighborCost
                    boarderNodes[neighborNode]['path'] = [[]]
                    addPath(boarderNodes,neighborNode,path)
                elif(boarderNodes[neighborNode]['cost'] == cost+neighborCost):
                    mergePath(boarderNodes,neighborNode,path,topology)
        
        # goal check -> is goal in visited Nodes
        if endPoint in visitedNodes:
            return visitedNodes[endPoint];
        
        #EndLoop

    return 0
        
def addPath(boarderNodes,neighborNode,path):
    boarderNodes[neighborNode]['path'] = []
    for i in path:
        line = []
        for j in i:
            line.append(j)
        line.append(neighborNode)
        boarderNodes[neighborNode]['path'].append(line)
        
def mergePath(boarderNodes,neighborNode,path,topology):
    smallest = len(topology);
    for i in path:
        if(len(i)+1 < smallest):
            smallest = len(i)+1
    for i in boarderNodes[neighborNode]['path']:
        if(len(i) < smallest):
            smallest = len(i)

    for i in path:
        line = []
        for j in i:
            line.append(j)
        line.append(neighborNode)
        boarderNodes[neighborNode]['path'].append(line)
        
    for i in boarderNodes[neighborNode]['path']:
        if(len(i) > smallest):
            boarderNodes[neighborNode]['path'].remove(i)
    
    
    
    
    
    

