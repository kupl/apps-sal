# cook your dish here
t = int(input())
for x in range(t):
    n = int(input())
    l = [int(i) for i in input().split()]
    for i in l:
        if(i < 0):
            print("NO")
            break
    else:
        print("YES")
