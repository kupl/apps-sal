try:

    for i in range(int(input())):
        N, P = map(int, input().split())
        l = list(map(int, input().strip().split()))

        a = b = 0
        for j in l:
            if j >= int(P / 2):
                a += 1
            elif j <= int(P / 10):
                b += 1

        if(a == 1 and b == 2):
            print("yes")
        else:
            print("no")
except:
    pass
