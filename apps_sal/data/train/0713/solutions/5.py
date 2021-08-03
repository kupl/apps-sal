for i in range(int(input())):
    n = int(input())
    l1 = [int(i) for i in input().split()]
    m = int(input())
    l2 = [int(i) for i in input().split()]
    i = j = 0
    while(i < n and j < m):
        if(l1[i] == l2[j]):
            j += 1
        i += 1

    if(j == m):
        print("Yes")
    else:
        print("No")
