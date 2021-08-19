for _ in range(int(input())):
    n = int(input())
    arr1 = list(set(map(int, input().split())))
    sum = 0
    for i in arr1:
        if i % 6 == 0:
            sum += 6
        else:
            sum += i % 6
    print(sum)
