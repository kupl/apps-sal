t = int(input())
roses = 0
for i in range(t):
    B,G= list(map(int,input().split()))
    roses = 2*G + 2*(B -1)
    print(roses)


