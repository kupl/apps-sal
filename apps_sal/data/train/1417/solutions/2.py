try:
    for _ in range(int(input())):
        n = input()
        arr = list(map(int, input().split()))
        s = [1, 2, 3, 4, 5, 6, 7, 8]
        mini = 100000
        for x in s:
            coun = arr.count(x)
            if coun < mini:
                mini = coun
        print(mini)
except:
    pass
