from itertools import permutations
def friend_find(line):
    p=list(set(permutations(['red','blue','blue'],3)))
    f=i=0
    while i<len(line):
        x=tuple(line[i:i+3])
        if x in p:
            f+=1
            i+=x.index('red')
        i+=1
    return f

