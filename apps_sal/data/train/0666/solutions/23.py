# cook your dish here
# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print("1")
    else:
        p=1
        for i in range(n):
            for j in range(n):
                print(p,end='')
                p+=1
            print()
                
