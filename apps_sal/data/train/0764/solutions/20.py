t = int(input())
while t > 0:
    str_1 = set(input().split())
    str_2 = set(input().split())
    if len(str_1.intersection(str_2)) >= 2:
        print("similar")
    else:
        print("dissimilar")
    t -= 1
