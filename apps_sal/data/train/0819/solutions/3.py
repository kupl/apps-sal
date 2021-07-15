# cook your dish here
for t in range(int(input())):
    R, B = [int(i) for i in input().split(" ")]
    while(R > 1 and B > 1):
        if R > B:
            R = R - (B * int(R/B))
        elif R < B:
            B = B - (R * int(B/R))
        else:
            break
        # print("R: " + str(R) + " B: " + str(B))
    if R == 1 or B == 1:
        print("YES")
    else:
        print("NO")
