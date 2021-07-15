# cook your dish here
for _ in range(int(input())):
    n=int(input())
    for i in range(n+1):
        for j in range(i+1):
            if j==i:
                print(i,end='')
            else:
                print("*",end='')
        print()
