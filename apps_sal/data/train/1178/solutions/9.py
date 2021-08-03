for _ in range(int(input())):
    n = int(input())
    list1 = list(map(int, input().split()))
    sum = 0
    list1.sort()
    for i in range(len(list1)):
        if list1[i] <= i:
            sum = sum + 1
        else:
            break
    print(sum)
