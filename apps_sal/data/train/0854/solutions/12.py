def c(data):
    n,d=data
    return 'prekrasnyy'if len(set(d))==n else'ne krasivo'
def l(): return [(int(input()), [int(x) for x in input().split()]) for _ in range(int(input()))]
def __starting_point():
    print('\n'.join(map(c,l())))
__starting_point()
