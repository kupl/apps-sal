try:
    for _ in range(int(input())):
        list1 = [int(x) for x in input().split()]
        n2 = list1[0] + list1[1] - list1[3]
        n1 = list1[0] - n2
        n3 = list1[2] - n1
        print(n1, n2, n3)
except:
    pass
