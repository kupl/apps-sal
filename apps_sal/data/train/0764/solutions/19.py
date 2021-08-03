# cook your dish here
T = int(input())
for i in range(T):
    dish1 = list(input().split())
    dish2 = list(input().split())
    similar = 0
    for i in (dish1):
        for j in (dish2):
            if i == j:
                similar = similar + 1
    if similar >= 2:
        print("similar")
    else:
        print("dissimilar")
