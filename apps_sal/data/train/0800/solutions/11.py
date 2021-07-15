n=int(input())
l=[int(i) for i in input().split()][:n]
l=sorted(l)
print(l[-1],l[0])
