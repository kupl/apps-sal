N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]
print(0 if all([a==b for a,b in AB]) else sum([b for a,b in AB])-min([b for a,b in AB if a>b]))
