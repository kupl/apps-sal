from bisect import bisect_left as BL

n = int(input())
graph = [(-99**9, 0, 0)] # x, y, slope
for i,a in enumerate(map(int,input().split())):
    a-= i
    new = []
    turnj = BL(graph, (a,99**9)) - 1
    
    # add |x-a|
    for j in range(turnj):
        x, y, sl = graph[j]
        new.append((x, y+(a-x), sl-1))
    for j in range(turnj, len(graph)):
        x, y, sl = graph[j]
        if j == turnj:
            new.append((x, y+(a-x), sl-1))
            new.append((a, y+(a-x)+(sl-1)*(a-x), sl+1))
        else: new.append((x, y+(x-a), sl+1))
    
    # remove positive slopes
    graph = new
    while graph[-1][2] > 0: x, y, sl = graph.pop()
    if graph[-1][2] != 0: graph.append((x, y, 0))
print(graph[-1][1])
