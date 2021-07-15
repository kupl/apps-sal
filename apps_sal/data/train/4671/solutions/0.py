def isTree(matrix):
    visited_nodes = set([0])
    crossed_edges = set()
    agenda = [0]

    while agenda:
        node = agenda.pop()
        for i in matrix[node]:
            if (node, i) in crossed_edges: continue 
            if i in visited_nodes: return False
            agenda.append(i)
            crossed_edges.add( (i, node) )
            visited_nodes.add(i)
    
    return len(visited_nodes) == len(matrix)
