def c(data):
    n,d=data
    elem=[]
    for i in d:
        if i in elem:
            return 'ne krasivo'
        elem.append(i)
    else:
        return 'prekrasnyy'

def l(): return [(int(input()), [int(x) for x in input().split()]) for _ in range(int(input()))]
def __starting_point():
    print('\n'.join(map(c,l())))
__starting_point()
