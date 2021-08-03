# cook your dish here
t = int(input())
for _ in range(t):
    s1 = []
    s2 = []
    c = 0
    s1 = list(input().split())
    s2 = list(input().split())
    for i in range(len(s1)):
        if(s1[i] in s2):
            c = c + 1
    if(c >= (len(s1) / 2)):
        print("similar")
    else:
        print("dissimilar")
