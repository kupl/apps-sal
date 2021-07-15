from bisect import bisect_left as BL

n = int(input())
graph = [(-99**9, 0)] # x, slope
ans = 0
for i,a in enumerate(map(int,input().split())):
    a-= i
    new = []
    turnj = BL(graph, (a,99**9)) - 1
    if turnj != len(graph)-1:
        ans+= graph[-1][0] - a
    
    # add |x-a|
    for j in range(turnj):
        x, sl = graph[j]
        new.append((x, sl-1))
    for j in range(turnj, len(graph)):
        x, sl = graph[j]
        if j == turnj:
            new.append((x, sl-1))
            new.append((a, sl+1))
        else: new.append((x, sl+1))
    
    # remove positive slopes
    graph = new
    while graph[-1][1] > 0: x, sl = graph.pop()
    if graph[-1][1] != 0: graph.append((x, 0))
print(ans)
