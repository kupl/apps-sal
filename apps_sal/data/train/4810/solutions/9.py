def make_spanning_tree(edges, t):
    X = [edges[0][0][0]]
    output = []
    while True:
        val = float("inf") if t == "min" else -float("inf")
        current = new_X = None
        for node in X:
            for edge in edges:
                if t == "min":
                    if edge[0][0] == node:
                        if edge[1] <= val and edge[0][1] not in X:
                            val, current, new_X = edge[1], edge, edge[0][1]
                    elif edge[0][1] == node:
                        if edge[1] <= val and edge[0][0] not in X:
                            val, current, new_X = edge[1], edge, edge[0][0]
                else:
                    if edge[0][0] == node:
                        if edge[1] >= val and edge[0][1] not in X:
                            val, current, new_X = edge[1], edge, edge[0][1]
                    elif edge[0][1] == node:
                        if edge[1] >= val and edge[0][0] not in X:
                            val, current, new_X = edge[1], edge, edge[0][0]
        if new_X is None:
            break
        X.append(new_X)
        output.append(current)
    return output
