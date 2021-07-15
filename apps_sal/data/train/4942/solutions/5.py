def directions(goal):
    y=sum(1 if d=='N' else -1 if d=='S' else 0 for d in goal)
    x=sum(1 if d=='E' else -1 if d=='W' else 0 for d in goal)
    return list(('N' if y>0 else 'S')*abs(y) + ('E' if x>0 else 'W')*abs(x))
