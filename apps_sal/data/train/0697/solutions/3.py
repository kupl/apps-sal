ncases = int(input())

for cases in range(ncases):
    players, selected = list( map( int, input().split()))
    powerlist = list( map( int, input().split()))
    currmax = sum(powerlist[:selected])
    change = 0
    for i in range(selected, players):
        change += powerlist[i]
        change -= powerlist[i - selected]
        if change > 0:
            currmax += change
            change = 0
    print(currmax)
