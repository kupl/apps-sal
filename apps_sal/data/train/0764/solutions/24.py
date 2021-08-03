t = int(input())
for i in range(t):
    a = input().split()
    b = input().split()
    c = 0
    for i in a:
        if(i in b):
            c = c + 1
    if(c >= 2):
        print("similar")
    else:
        print("dissimilar")
