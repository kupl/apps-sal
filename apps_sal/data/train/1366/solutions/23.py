def count(lst):
    for i in range(0,len(lst)):
        if lst[-1]==0:
            lst.pop()
        elif lst[0]==0:
            lst.pop(0)
            
        else:
            break
    if lst.count(0)==len(lst):
        print("1")
    else:
        print(len(lst))


for i in range(int(input())):
    n = int(input())
    lst = list(map(int,input().split()))
    count(lst)
