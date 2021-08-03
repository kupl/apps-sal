# cook your dish here
t = int(input())
for _ in range(t):
    a = set(input().split())
    b = set(input().split())
    if len(a.intersection(b)) >= 2:
        print("similar")
    else:
        print("dissimilar")
