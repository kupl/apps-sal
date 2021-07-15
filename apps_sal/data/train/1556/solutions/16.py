# cook your dish here

# cook your dish here
t = int(input())

while t:
    n = int(input())


    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j % 2 == 1:
                print(1, end='')
            else:
                print(0, end='')
            
        print()
        
    t -= 1
