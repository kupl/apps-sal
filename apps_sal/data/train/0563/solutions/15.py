for i in range(int(input())):
    nlands=int(input())
    maxcoins=list(map(int,input().split()))
    for j in range(int(input())):
        trips=list(map(int,input().split()))
        print(sum(maxcoins[trips[0]-1:trips[1]]))
