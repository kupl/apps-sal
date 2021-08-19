for i in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    lst1 = [i for i in range(n)]
    dict1 = {}.fromkeys(lst1, 0)
    for key in lst:
        dict1[key] += 1
    for key in dict1:
        if dict1[key] > 0:
            print(key, end=' ')
        else:
            print(0, end=' ')
    print()
