# cook your dish here
t = int(input())
i = 0
while i < t:
    a = []
    a = input().split()
    b = []
    b = input().split()
    j = 0
    c = 0
    while j < 4:
        if a[j] in b:
            c += 1
        j += 1
    if c >= 2:
        print("similar")
    else:
        print("dissimilar")
    i += 1
