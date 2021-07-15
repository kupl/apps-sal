for _ in range(int(input())):
    n = int(input())
    print(0)
    x = 1
    for i in range(n):
        print('*'*x+str(x))
        x+=1
