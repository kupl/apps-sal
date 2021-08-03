try:
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        s = sum(a)
        if(s % n == 0):
            print("Yes")
        else:
            print("No")
except:
    pass
