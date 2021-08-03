t = int(input())
for i in range(0, t):
    s1 = input().lower()
    s2 = input().lower()
    if(s1 < s2):
        print("first")
    elif(s1 > s2):
        print("second")
    else:
        print("equal")
