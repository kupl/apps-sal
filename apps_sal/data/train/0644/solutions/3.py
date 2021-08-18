for i in range(int(input())):
    n = int(input())
    m = [int(i) for i in input().split()]
    chk = sum(m)
    if(chk % n == 0):
        print("Yes")
    else:
        print("No")
