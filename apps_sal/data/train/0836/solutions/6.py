for _ in range(eval(input())):
    n = eval(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    (max1, index, rc) = (0, 0, 0)
    for i in range(len(l)):
        temp = l[i] * r[i]
        if max1 < temp or (max1 == temp and r[i] > rc):
            max1 = temp
            rc = r[i]
            index = i
    print(index + 1)
