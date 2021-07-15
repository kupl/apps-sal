def directions(goal):
    ans=[]
    ns = goal.count('N') - goal.count('S')
    if ns>0: ans.extend(ns*['N'])
    if ns<0: ans.extend(-ns*['S'])
    ew = goal.count('E') - goal.count('W')
    if ew>0: ans.extend(ew*['E'])
    if ew<0: ans.extend(-ew*['W'])
    return ans
