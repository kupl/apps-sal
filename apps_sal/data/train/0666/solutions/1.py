def P(h):
    number=1
    for i in range(1, h + 1):
        for j in range(1, h + 1):
            print(number, end = '')
            number = number + 1
        print()

for i in range(int(input())):
    a=int(input())
    P(a)
    
