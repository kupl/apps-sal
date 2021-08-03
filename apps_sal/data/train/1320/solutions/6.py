# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if(n == 1 or n % 2 == 0):
        print('B')
        continue
    elif(n == 3):
        print('A')
        continue
    else:
        if((n - 3) % 2 == 0):
            print('B')
        else:
            print('A')
