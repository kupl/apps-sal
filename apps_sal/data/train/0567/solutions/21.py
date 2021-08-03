from collections import Counter
T = int(input())
for i in range(T):
    N = int(input())
    List = [int(x) for x in input().split()]
    Initial = List[0]
    a = 0
    count = 0
    for i in List:
        if(Initial == i):
            count += 1
            if(count >= 3):
                a = 1
                break
        if(Initial != i):
            count = 1
        Initial = i
    if(a == 1):
        print("Yes")
    else:
        print("No")
