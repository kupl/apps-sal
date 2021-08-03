n = int(input())
for i in range(0, n):
    l1 = list(input().split())
    l2 = list(input().split())
    l3 = []
    for item in l1:
        if(item in l2):
            l3.append(item)

    if(len(l3) >= 2):
        print("similar")
    else:
        print("dissimilar")
