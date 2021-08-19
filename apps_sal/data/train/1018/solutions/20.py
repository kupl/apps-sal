a = int(input())
while a != 0:
    b = int(input())
    mylist = list(map(int, input().split()))
    min = mylist[0] - mylist[1]
    for i in range(len(mylist) - 1):
        p = mylist[i] - mylist[i + 1]
        if p < min:
            min = p
    print(min)
    a -= 1
