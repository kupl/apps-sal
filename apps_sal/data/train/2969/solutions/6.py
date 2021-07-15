def advice(agents, n):
    agents = { (x,y) for x,y in agents if 0<=x<n and 0<=y<n }
    town = { (x,y) for x in range(n) for y in range(n)}
    if agents==town: return []
    while agents and town>agents:
        town -= agents
        agents = {pos for x,y in agents for pos in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)) if pos in town }
    return sorted(town)
