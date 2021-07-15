from itertools import chain
def tv_remote(word):
    locs=list(chain.from_iterable([(j,i) for j in range(0,8)] for i in range(0,5)))
    lookup=dict(zip("abcde123fghij456klmno789pqrst.@0uvwxyz_/",locs))
    prev_loc=lookup[word[0]]
    dist=sum(prev_loc)
    for l in word[1:]:
        loc=lookup[l]
        dist+=abs(loc[0]-prev_loc[0])+abs(loc[1]-prev_loc[1])
        prev_loc=loc
    
    return dist+len(word)
