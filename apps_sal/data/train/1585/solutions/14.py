for _ in range(int(input())):
    a, b = map(int, input().split(' '))
    if(a > b):
        print(a, end=" ")
    if(b > a):
        print(b, end=" ")
    print(a + b)
