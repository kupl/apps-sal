try:
    for _ in range(int(input())):
        n = int(input())
        lis = list(map(int, input().split()))
        flag = 0
        for i in range(n - 2):
            if(lis[i] == lis[i + 1] == lis[i + 2]):
                flag = 1
                break
            else:
                continue
        if(flag == 1):
            print("Yes")
        else:
            print("No")
except Exception:
    pass
