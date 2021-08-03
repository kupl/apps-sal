n = int(input())
while(n > 0):
    n -= 1
    a = int(input())
    for i in range(a + 1):
        print("*" * i, end='')
        print(i)
