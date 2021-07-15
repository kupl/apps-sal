from heapq import heappush as push, heappop as pop

def shortestPath(topology, startPoint, endPoint):
    current, res = [], (float('inf'), None, [])
    push(current, (0, 1, [startPoint]))
    while current:
        time, size, path = pop(current)
        if time > res[0] or time == res[0] and size > res[1]:
            return res[2]
        if path[-1] == endPoint:
            if time < res[0] or size < res[1]:
                res = (time, size, [path])
            else:
                res[2].append(path)
        else:
            for k,v in topology[path[-1]].items():
                if k not in path:
                    push(current, (time+v, size+1, path+[k]))
    return "No path"
