def filtering(lst):
    new_lst = set()
    vertices = []
    for item in lst:
        if item[0][0] not in vertices:
            vertices.append(item[0][0])
        if item[0][1] not in vertices:
            vertices.append(item[0][1])
        if item[0][0] == item[0][1]:
            continue
        else:
            new_lst.add(item)
    return [new_lst, vertices]
    
def poss_edg_func(vert, edges):
    res = []
    for edge in edges:
        if edge[0][0] in vert and edge[0][1] not in vert:
            res.append(edge)
        if edge[0][1] in vert and edge[0][0] not in vert:
            res.append(edge)
    return res
            
def make_spanning_tree(edges, t):
    temp = filtering(edges)
    edg, vert = temp[0], temp[1]
    path = [eval(t)(edg, key = lambda x: x[1])]
    while len(path) != len(vert) - 1:
        used_vert = set([char for v in path for char in v[0]])
        poss_edg = poss_edg_func(used_vert, edg)
        path.append(eval(t)(poss_edg, key = lambda x: x[1]))
    return path
        
    
    

