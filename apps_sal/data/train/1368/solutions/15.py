t = int(input())
for i in range(t):
    ac, mi = map(int, input().split(" "))
    if(ac >= mi):
        print("Yes")
    else:
        print("No")
