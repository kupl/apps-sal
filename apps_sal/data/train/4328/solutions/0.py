def redWith2Blues(i, line):
    return any(line[i-2+x:i+1+x].count('blue')==2 for x in range(3))

def friend_find(line):
    return sum( p=='red' and redWith2Blues(i,line) for i,p in enumerate(line))
