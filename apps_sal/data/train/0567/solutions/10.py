# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    flag = 0
    for i in range(n - 2):
        if(l[i] == l[i + 1] and l[i] == l[i + 2]):
            print("Yes")
            flag = 1
            break
    if(flag == 0):
        print("No")
