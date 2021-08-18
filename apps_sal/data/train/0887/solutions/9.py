for i in range(int(input())):
    n = int(input())
    x = 0
    l1 = list(map(float, input().split()))
    l2 = list(map(float, input().split()))
    if l1[0] == 0 and l2[n - 1] == 0 and l1[n - 1] == l2[0]:
        for j in range(1, n - 1):
            if(l1[j] == 0 or l2[j] == 0):
                x = 1
                break
            if l2[0] > (l1[j] + l2[j]):
                x = 1
                break
            if l1[j] > (l2[j] + l2[0]):
                x = 1
                break
            if l2[j] > (l1[j] + l2[0]):
                x = 1
                break
    else:
        x = 1
    if x == 0:
        print("Yes")
    else:
        print("No")
