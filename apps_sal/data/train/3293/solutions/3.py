age = lambda cur: int(sum(cur) == 1 or cur == (0,1,1))
def rule30(l, n):
    if n <= 0: return l
    l = [0,0] + l + [0,0]
    return rule30([age(cur) for cur in zip(l[:-2],l[1:-1],l[2:])], n-1)

