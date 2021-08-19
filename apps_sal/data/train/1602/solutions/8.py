# cook your dish here
# cook your dish here# cook your dish here
t = int(input())

for _ in range(t):
    d = int(input())
    s = int(input())
    e = list(map(int, input().split()))

    for i in e:
        if(i == 1):
            flag = 1
            break
        else:
            flag = 0
    if(flag == 1):
        print("Impossible")
    else:
        print("Possible")
