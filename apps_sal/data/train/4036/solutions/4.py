def days_represented(trips):
    total = 0
    visited = []
    for i in range(len(trips)):
        trip = trips[i]
        arrival = trip[1]
        departure = trip[0]
        for j in range(departure, arrival + 1):
            if j not in visited:
                visited.append(j)
            else:
                continue
    return len(visited)
