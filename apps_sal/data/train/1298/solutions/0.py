t = int(input())
while(t):
    n = int(input())
    ar = list(map(int, input().strip().split(" ")))
    print(len([x for x in ar[1:len(ar)] if ar[0] < x]))
    t -= 1
