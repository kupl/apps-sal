n=int(input())
frnd=[int(x) for x in input().split()]
tot=[int(x) for x in input().split()]
frnd.sort()
tot.sort()
for i in range (n+1):
    if (i==n):
        print(tot[i])
    elif (frnd[i]!=tot[i]):
        print(tot[i])
        break
